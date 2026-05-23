"""
Listwise Judge — batch-scoring of multiple responses.
Used by: SurGE (batch pointwise scoring).
Supports dataset-specific prompt formats via YAML templates.
"""
import json
from .base_judge import BaseJudge


class ListwiseJudge(BaseJudge):
    """Batch scoring judge for multiple responses."""

    def judge(self, instruction: str, responses: list,
              prompt_template: dict, data_id=None, format_kwargs: dict = None) -> list:
        """
        Score all responses in one call.
        Returns [{"data_id": ..., "models": [...], "judge_result": {...}}, ...]
        """
        format_kwargs = format_kwargs or {}
        system_prompt = prompt_template.get("task_description", "")
        user_prompt_format = prompt_template.get("user_prompt_format", "")
        output_format = prompt_template.get("output_format", "")

        # Replace {instruction}
        user_prompt = user_prompt_format.replace("{instruction}", instruction)

        # Replace {response_0}, {response_1}, ... with corresponding content
        for i, resp in enumerate(responses):
            user_prompt = user_prompt.replace(f"{{response_{i}}}", resp['content'])
        user_prompt = user_prompt.replace("{output_format}", output_format)

        # Replace additional format_kwargs (e.g., {title_A}, {text_A}, {reference})
        user_prompt = self._apply_format_kwargs(user_prompt, format_kwargs)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        raw_output = self.client.chat(messages, self.model_name,
                                      temperature=self.config.get("temperature", 0.0),
                                      max_tokens=self.config.get("max_tokens", 4096))

        parsed = self.parse_response(raw_output)
        return [{
            "data_id": data_id,
            "models": [r["model"] for r in responses],
            "judge_result": parsed,
        }]

    def parse_response(self, raw_output: str) -> dict:
        """Parse JSON-formatted scoring result."""
        try:
            cleaned = self._clean_response(raw_output)
            return self._extract_json(cleaned)
        except (json.JSONDecodeError, AttributeError):
            return {"raw": raw_output, "error": "parse_failed"}
