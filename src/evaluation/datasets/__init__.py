"""Dataset module registry."""
import importlib

REGISTRY = {
    "deepresearch_bench": "src.evaluation.datasets.deepresearch_bench",
    "realdr": "src.evaluation.datasets.realdr",
    "surge": "src.evaluation.datasets.surge",
    "wp_bench": "src.evaluation.datasets.wp_bench",
    "ma": "src.evaluation.datasets.ma",
    "verify_bench_hard": "src.evaluation.datasets.verify_bench_hard",
}


def get_dataset_module(dataset: str):
    """Dynamically import and return a dataset module."""
    path = REGISTRY.get(dataset)
    if path is None:
        raise KeyError(f"Unknown dataset: {dataset}, available: {list(REGISTRY.keys())}")
    return importlib.import_module(path)
