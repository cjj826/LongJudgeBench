"""
API client base class + config loader.
"""
from abc import ABC, abstractmethod
from pathlib import Path
import json


class BaseClient(ABC):
    """Abstract base class for API clients."""

    def __init__(self, api_base: str, api_key: str):
        self.api_base = api_base
        self.api_key = api_key

    @abstractmethod
    def chat(self, messages: list, model: str,
             temperature: float = 0.0, max_tokens: int = 4096) -> str:
        """Call model and return response text."""
        pass


def load_api_config() -> dict:
    """Load API configuration from config/api_config.json."""
    config_path = Path(__file__).resolve().parent.parent.parent.parent / "config" / "api_config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_model_interfaces(api_config: dict, target_models: list = None) -> list:
    """
    Get model endpoints from api_config.
    Returns [{"name": model_name, "api_base": ..., "api_key": ...}, ...]
    """
    results = []
    for interface in api_config.get("api_interfaces", []):
        api_base = interface["api_base"]
        api_key = interface["api_key"]
        for model_entry in interface["judge_models"]:
            if isinstance(model_entry, dict):
                model_name = model_entry["model"]
                model_max_tokens = model_entry.get("max_tokens", 24576)
                model_max_prompt_tokens = model_entry.get("max_prompt_tokens")
                model_extra_body = model_entry.get("extra_body")
                model_api_model = model_entry.get("api_model")
            else:
                model_name = model_entry
                model_max_tokens = 24576
                model_max_prompt_tokens = None
                model_extra_body = None
                model_api_model = None
            if target_models is None or model_name in target_models:
                info = {
                    "name": model_name,
                    "api_base": api_base,
                    "api_key": api_key,
                    "max_tokens": model_max_tokens,
                }
                if model_max_prompt_tokens is not None:
                    info["max_prompt_tokens"] = model_max_prompt_tokens
                if model_extra_body is not None:
                    info["extra_body"] = model_extra_body
                if model_api_model is not None:
                    info["api_model"] = model_api_model
                results.append(info)
    return results
