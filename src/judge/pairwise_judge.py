"""
Pairwise Judge — compares two responses side-by-side.
Used by: Writing-Preference-Bench, MA.
Supports debiased evaluation (swap A/B and average).
"""
import json
from .base_judge import BaseJudge


class PairwiseJudge(BaseJudge):
    """Pairwise comparison judge."""

    def judge(self, instruction: str, responses: list,
              prompt_template: dict, data_id=None, debiased=False, format_kwargs: dict = None) -> list:
        """
        Compare two responses. When debiased=True, runs both (A,B) and (B,A)
        orderings and outputs 2 result rows for averaging during metrics.
        Returns [{"data_id": ..., "responses": [...], "judge_result": {...}}, ...]
        """
        if len(responses) != 2:
            return []

        if not debiased:
            return [self._judge_pair(instruction, responses, prompt_template, data_id, format_kwargs)]

        # Debiased: output both comparison orderings (2 rows)
        result_orig = self._judge_pair(instruction, responses, prompt_template, data_id, format_kwargs)
        result_orig["judge_result"]["swap_position"] = "original"
        result_orig["judge_result"]["debiased"] = True

        swapped = [responses[1], responses[0]]
        result_swap = self._judge_pair(instruction, swapped, prompt_template, data_id, format_kwargs)
        result_swap["judge_result"]["swap_position"] = "swapped"
        result_swap["judge_result"]["debiased"] = True

        return [result_orig, result_swap]

    def _judge_pair(self, instruction: str, responses: list,
                    prompt_template: dict, data_id=None, format_kwargs: dict = None) -> dict:
        """Single pairwise comparison (internal method)."""
        format_kwargs = format_kwargs or {}
        system_prompt = prompt_template.get("task_description", "")
        user_prompt_format = prompt_template.get("user_prompt_format",
            "## 指令\n{instruction}\n\n## 回复 A\n{response_0}\n\n## 回复 B\n{response_1}\n\n")
        output_format = prompt_template.get("output_format", "")

        user_prompt = user_prompt_format.replace("{instruction}", instruction)
        user_prompt = user_prompt.replace("{response_0}", responses[0]['content'])
        user_prompt = user_prompt.replace("{response_1}", responses[1]['content'])
        user_prompt = user_prompt.replace("{output_format}", output_format)
        user_prompt = self._apply_format_kwargs(user_prompt, format_kwargs)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        raw_output = self.client.chat(messages, self.model_name,
                                      temperature=self.config.get("temperature", 0.0),
                                      max_tokens=self.config.get("max_tokens", 4096))

        parsed = self.parse_response(raw_output)
        return {
            "data_id": data_id,
            "response_a": responses[0]["model"],
            "response_b": responses[1]["model"],
            "judge_result": parsed,
        }

    def parse_response(self, raw_output: str) -> dict:
        """Parse JSON-formatted selection result."""
        try:
            cleaned = self._clean_response(raw_output)
            return self._extract_json(cleaned)
        except (json.JSONDecodeError, AttributeError):
            return {"raw": raw_output, "error": "parse_failed"}
