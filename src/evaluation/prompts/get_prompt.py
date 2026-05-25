"""Prompt loader: reads from config/prompts/{dataset}/{prompt_mode}.yaml
Supports WP-Bench rubric dynamic genre adaptation.
For surge/ma datasets, prompt_mode must include the dimension prefix
(e.g., content_vanilla, structure_vanilla, insights_vanilla).
"""
from pathlib import Path
import yaml
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Datasets whose prompt files are prefixed by evaluation dimension
DIMENSION_DATASETS = {
    "surge": ["content", "structure"],
    "ma": ["insights"],
}


def list_prompt_modes(dataset: str = None) -> dict:
    """List available prompt modes, optionally filtered by dataset.

    Returns: {dataset: [prompt_mode, ...], ...}
    """
    prompts_dir = BASE_DIR / "config" / "prompts"
    result = {}
    for ds_dir in sorted(prompts_dir.iterdir()):
        if not ds_dir.is_dir():
            continue
        modes = []
        for f in sorted(ds_dir.glob("*.yaml")):
            modes.append(f.stem)
        if dataset is None or ds_dir.name == dataset:
            result[ds_dir.name] = modes
    return result


def resolve_prompt_mode(dataset: str, prompt_mode: str) -> str:
    """Validate and optionally auto-complete the prompt_mode for dimension-prefixed datasets.

    For surge/ma, if prompt_mode lacks a known dimension prefix, raises a
    helpful error listing available options.
    """
    prefixes = DIMENSION_DATASETS.get(dataset)
    if prefixes:
        has_prefix = any(prompt_mode.startswith(p + "_") for p in prefixes)
        if not has_prefix:
            # Check all available modes for this dataset
            all_modes = list_prompt_modes(dataset).get(dataset, [])
            if all_modes:
                # Suggest dimension-prefixed modes that match the requested suffix
                matching = [m for m in all_modes if m.endswith("_" + prompt_mode) or m == prompt_mode]
            else:
                matching = []
            if matching:
                return matching[0]
            examples = [f"{p}_{prompt_mode}" for p in prefixes]
            raise ValueError(
                f"Dataset '{dataset}' requires dimension-prefixed prompt modes. "
                f"Available: {', '.join(all_modes) if all_modes else '(none found)'}"
            )
    return prompt_mode


def get_prompt(dataset: str, prompt_mode: str, tag: str = None) -> dict:
    """Load prompt YAML file.

    Args:
        dataset: dataset name
        prompt_mode: prompt mode, e.g. vanilla, vanilla_reference,
                     or dimension-prefixed for surge/ma (content_vanilla, etc.)
        tag: WP-Bench genre tag (only needed for wp_bench rubric mode)
    """
    # Resolve dimension-prefixed mode if needed
    resolved_mode = resolve_prompt_mode(dataset, prompt_mode)

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
    path = BASE_DIR / "config" / "prompts" / dataset / f"{resolved_mode}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
