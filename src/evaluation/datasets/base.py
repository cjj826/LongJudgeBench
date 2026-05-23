"""BaseDataset interface definition."""


class BaseDataset:
    """Base class for datasets; subclasses must implement methods below."""

    @staticmethod
    def get_paradigm() -> str:
        """Return judge paradigm: pointwise / pairwise / listwise."""
        raise NotImplementedError

    @staticmethod
    def load_data(data_dir: str = None) -> list[dict]:
        """Load data, return a list of unified-format records.

        Each: {
            "id": ...,
            "instruction": "...",
            "responses": [{"model": ..., "content": ...}, ...],
            "dataset": "...",
            ...
        }
        """
        raise NotImplementedError

    @staticmethod
    def extract_metrics(judge_results: list, gt_data: list) -> dict:
        """Extract scores and compute grouped metrics.

        Returns: {"groups": {"all": {gt:[], pred:[]}, "model:X": {...}, ...}}
        For pairwise datasets additionally: {"accuracy": ..., "correct": N, "total": N}
        """
        raise NotImplementedError
