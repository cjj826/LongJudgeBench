"""
Pointwise Judge — scores each response independently.
Used by: DeepResearch-Bench, RealDR, VerifyBench.
Supports dataset-specific prompt formats via YAML templates.
"""
import json
from .base_judge import BaseJudge


class PointwiseJudge(BaseJudge):
    """Pointwise scoring judge."""

    def judge(self, instruction: str, responses: list,
              prompt_template: dict, data_id=None, format_kwargs: dict = None) -> list:
        """
        Score each response independently.
        Returns [{"data_id": ..., "model": ..., "response": ..., "judge_result": {...}}, ...]
        """
        system_prompt = prompt_template.get("task_description", "")
        user_prompt_format = prompt_template.get("user_prompt_format",
            "## 指令\n{instruction}\n\n## 回复\n{response_0}\n\n")
        output_format = prompt_template.get("output_format", "")
        format_kwargs = format_kwargs or {}

        results = []
        for resp in responses:
            user_prompt = user_prompt_format.replace("{instruction}", instruction)
            user_prompt = user_prompt.replace("{response_0}", resp['content'])
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
            results.append({
                "data_id": data_id,
                "model": resp["model"],
                "response": raw_output,
                "judge_result": parsed,
            })

        return results

    def parse_response(self, raw_output: str) -> dict:
        """Parse JSON-formatted scoring result."""
        try:
            cleaned = self._clean_response(raw_output)
            return self._extract_json(cleaned)
        except (json.JSONDecodeError, AttributeError):
            return {"raw": raw_output, "error": "parse_failed"}
