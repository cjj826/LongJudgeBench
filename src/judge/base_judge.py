"""Base class for LLM-as-Judge evaluation."""
from abc import ABC, abstractmethod
import json
import re


class BaseJudge(ABC):

    def __init__(self, model_name: str, client, config: dict):
        self.model_name = model_name
        self.client = client
        self.config = config

    @abstractmethod
    def judge(self, instruction: str, responses: list, prompt_template: dict, **kwargs) -> dict:
        """Run evaluation and return results."""
        pass

    def _apply_format_kwargs(self, template: str, format_kwargs: dict = None) -> str:
        """Inject extra {key} placeholders into the prompt template."""
        if not format_kwargs:
            return template
        result = template
        for key, value in format_kwargs.items():
            placeholder = "{" + key + "}"
            result = result.replace(placeholder, str(value))
        return result

    @abstractmethod
    def parse_response(self, raw_output: str) -> dict:
        """Parse model output into structured result."""
        pass

    @staticmethod
    def _clean_response(raw_output: str) -> str:
        """Remove <think> reasoning tags and trim whitespace."""
        cleaned = re.sub(r'<think>.*?</think>', '', raw_output, flags=re.DOTALL)
        return cleaned.strip()

    @staticmethod
    def _extract_json(text: str) -> dict:
        """
        Extract JSON object from text. Tries:
        1. ```json ... ``` code blocks
        2. Direct json.loads
        3. Iterative {}-from-right matching (handles truncated JSON and LaTeX-wrapped text)
        """
        # Strategy 1: code block
        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        # Strategy 2: direct parse
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass
        starts = [i for i, ch in enumerate(text) if ch == '{']
        ends = [i for i, ch in enumerate(text) if ch == '}']
        for s in reversed(starts):
            for e in reversed(ends):
                if e <= s:
                    break
                try:
                    return json.loads(text[s:e + 1])
                except json.JSONDecodeError:
                    continue
        raise json.JSONDecodeError("No JSON found", text, 0)
