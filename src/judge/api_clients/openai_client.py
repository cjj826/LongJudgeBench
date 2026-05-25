"""
OpenAI-compatible API client.
Does NOT truncate input — oversized prompts are caught by the API and
logged as token_exceed by the caller for error-rate statistics.
"""
from openai import OpenAI
from .base_client import BaseClient


class OpenAIClient(BaseClient):
    """OpenAI-compatible API client."""

    def __init__(self, api_base: str = "", api_key: str = "EMPTY",
                 max_prompt_tokens: int = 120000, extra_body: dict = None,
                 api_model: str = None):
        super().__init__(api_base, api_key)
        self.client = OpenAI(api_key=self.api_key, base_url=self.api_base) if self.api_base else OpenAI(api_key=self.api_key)
        self.max_prompt_tokens = max_prompt_tokens
        self.extra_body = extra_body or {}
        self.api_model = api_model

    def chat(self, messages: list, model: str,
             temperature: float = 0.0, max_tokens: int = 4096) -> str:
        actual_model = self.api_model or model
        kwargs = dict(
            model=actual_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        if self.extra_body:
            kwargs["extra_body"] = self.extra_body

        # DashScope requires streaming when enable_thinking is set
        use_stream = self.extra_body and self.extra_body.get("enable_thinking") is True
        if use_stream:
            kwargs["stream"] = True
            kwargs["stream_options"] = {"include_usage": True}
            response = self.client.chat.completions.create(**kwargs)
            content = ""
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                    content += chunk.choices[0].delta.content
            return content
        else:
            response = self.client.chat.completions.create(**kwargs)
            return response.choices[0].message.content
