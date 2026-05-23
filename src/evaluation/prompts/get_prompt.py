"""Prompt loader: reads from config/prompts/{dataset}/{prompt_mode}.yaml
Supports WP-Bench rubric dynamic genre adaptation
"""
from pathlib import Path
import yaml
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


def get_prompt(dataset: str, prompt_mode: str, tag: str = None) -> dict:
    """Load prompt YAML file.

    Args:
        dataset: dataset name
        prompt_mode: prompt mode (vanilla / rubric)
        tag: WP-Bench genre tag (only needed for wp_bench rubric mode)
    """
    # ── WP-Bench rubric dynamic loading (from vanilla_rubric.yaml) ──
    if dataset == "wp_bench" and ("rubric" in prompt_mode or prompt_mode == "rubric"):
        path = BASE_DIR / "config" / "prompts" / "wp_bench" / "vanilla_rubric.yaml"
        if not path.exists():
            raise FileNotFoundError(f"WP-Bench rubric file not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            prompt = yaml.safe_load(f)

        if tag:
            # Read tag -> genre mapping
            rubric_dir = BASE_DIR / "config" / "prompts" / "wp_bench" / "rubric"
            mapping_path = rubric_dir / "tag_to_genre.json"
            if mapping_path.exists():
                with open(mapping_path, "r", encoding="utf-8") as f:
                    tag_map = json.load(f)
                genre = tag_map.get(tag, "fiction")
            else:
                genre = "fiction"

            # Replace placeholder (substitute {genre} in user_prompt_format)
            if prompt and "user_prompt_format" in prompt:
                prompt["user_prompt_format"] = prompt["user_prompt_format"].replace(
                    "{genre}", genre
                )

                # Load genre-specific criteria
                genre_criteria_path = rubric_dir / f"genre_{genre}.yaml"
                if genre_criteria_path.exists():
                    with open(genre_criteria_path, "r", encoding="utf-8") as f:
                        genre_data = yaml.safe_load(f)
                    genre_criteria = genre_data.get("genre_criteria", "") if genre_data else ""
                    if genre_criteria and "user_prompt_format" in prompt:
                        prompt["user_prompt_format"] = prompt["user_prompt_format"].replace(
                            "{genre_criteria}", genre_criteria
                        )

        return prompt

    # ── Regular loading ──
    path = BASE_DIR / "config" / "prompts" / dataset / f"{prompt_mode}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
