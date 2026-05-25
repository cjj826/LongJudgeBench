"""
Reliability metrics — human-judge agreement.
"""
import itertools
import numpy as np
from scipy.stats import spearmanr, kendalltau


def kendalls_tau(rank1: list, rank2: list) -> float:
    """Kendall's Tau-b (handles ties, scipy default variant='b')."""
    tau, _ = kendalltau(rank1, rank2)
    return tau


def spearman_corr(x: list, y: list) -> float:
    """Spearman rank correlation."""
    corr, _ = spearmanr(x, y)
    return corr


def pairwise_accuracy(gt_scores: np.ndarray, pred_scores: np.ndarray) -> tuple:
    """
    Pairwise accuracy: for all C(n,2) pairs, check if (which is better in GT)
    matches (which is better in prediction).

    Args:
        gt_scores: human ground truth scores (n,)
        pred_scores: judge predicted scores (n,)

    Returns:
        (accuracy, correct_count, total_pairs)
    """
    correct = 0
    total = 0
    n = len(gt_scores)
    for i, j in itertools.combinations(range(n), 2):
        g = np.sign(gt_scores[i] - gt_scores[j])
        p = np.sign(pred_scores[i] - pred_scores[j])
        if np.isnan(g) or np.isnan(p):
            continue
        total += 1
        if g == 0 and p == 0:
            correct += 1  # mutual tie: judge agrees with GT
            total += 1
            continue
        if g == 0 or p == 0:
            continue  # one-sided tie → counted as 0 correct
        if g == p:
            correct += 1
    if total == 0:
        return np.nan, 0, 0
    return float(correct / total), correct, total


def average_per_query_accuracy(per_query_data: dict) -> dict:
    """
    Compute pairwise_accuracy per query, then aggregate all queries.

    per_query_data: {query_id: {"gt": [float, ...], "pred": [float, ...]}}

    Returns: {"accuracy": float or None, "correct": int, "total": int}
    """
    total_correct = 0
    total_pairs = 0
    for qid, data in per_query_data.items():
        gt = data.get("gt", [])
        pred = data.get("pred", [])
        if len(gt) < 2:
            continue
        acc, correct, pairs = pairwise_accuracy(np.array(gt), np.array(pred))
        if not np.isnan(acc):
            total_correct += correct
            total_pairs += pairs

    if total_pairs == 0:
        return {"accuracy": None, "correct": 0, "total": 0}

    return {
        "accuracy": round(total_correct / total_pairs, 4),
        "correct": total_correct,
        "total": total_pairs,
    }


def average_per_query_metrics(per_query_data: dict) -> dict:
    """
    Compute Spearman/Kendall per query, then average across queries.
    Each query needs >= 3 samples with >= 2 distinct values in both gt and pred.

    per_query_data: {query_id: {"gt": [float, ...], "pred": [float, ...]}}

    Returns:
        {spearman, kendall, n_queries_spearman, n_queries_kendall}
        spearman/kendall are None if not computable.
    """
    spearmans = []
    kendalls = []
    for qid, data in per_query_data.items():
        gt = data.get("gt", [])
        pred = data.get("pred", [])
        if len(gt) < 3 or len(pred) < 3:
            continue
        # Need at least 2 distinct values; scipy returns NaN for constant input, skip
        if len(set(gt)) < 2 or len(set(pred)) < 2:
            continue
        sp = spearman_corr(gt, pred)
        kt = kendalls_tau(gt, pred)
        if sp is not None and not (isinstance(sp, float) and np.isnan(sp)):
            spearmans.append(sp)
        if kt is not None and not (isinstance(kt, float) and np.isnan(kt)):
            kendalls.append(kt)

    return {
        "spearman": round(float(np.mean(spearmans)), 4) if spearmans else None,
        "kendall": round(float(np.mean(kendalls)), 4) if kendalls else None,
        "n_queries_spearman": len(spearmans),
        "n_queries_kendall": len(kendalls),
    }


