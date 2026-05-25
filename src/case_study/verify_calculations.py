"""
Verification script for analysis.md calculation claims.

Usage: PYTHONIOENCODING=utf-8 py -3 src/case_study/verify_calculations.py

This script verifies all numerical claims in analysis.md (English) and
analysis.zd.md (Chinese). Key findings are documented in the comments.

Key findings summary:
1. MAE table: original used rubric+reference mode + simple avg (not weighted)
   → confirmed: 7/8 models match exactly, qwen3-32b-nothinking had wrong values
2. Case A1/B2/Pattern(c): "rubric" labels should be "rubric+reference"
3. Verify_bench_hard: "all judges correct" and "mixed" were swapped
4. D2-Semantic/B2 error rates were incorrect
"""
import json
from pathlib import Path
from collections import defaultdict, Counter

BASE = Path(__file__).resolve().parent.parent.parent

def load_jsonl(path):
    items = []
    with open(str(path), 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items

def dim_simple_avg(jr, dim):
    """Simple average of target_scores within a dimension."""
    items = jr.get(dim, [])
    if not items:
        return None
    scores = [c.get('target_score') or c.get('article_2_score') for c in items]
    scores = [s for s in scores if s is not None]
    if not scores:
        return None
    return sum(scores) / len(scores)


# 1. MAE TABLE verification
print("=" * 70)
print("1. Cross-Model MAE Table (rubric+reference, simple avg)")
print("=" * 70)

gts = {d['id']: d for d in load_jsonl(BASE / 'ground_truth' / 'deepresearch_bench_gt.jsonl')}
models_list = ['gpt-5.2', 'gpt-4o-mini', 'deepseek-v4-flash', 'qwen3-max',
               'qwen3-32b', 'qwen3-32b-nothinking', 'kimi-k2.6', 'glm-5.1']

for model in models_list:
    results = load_jsonl(BASE / f'outputs/judge_results/{model}/deepresearch_bench/vanilla_rubric_reference.jsonl')
    sum_ae = dict.fromkeys(['instruction_following', 'insight', 'comprehensiveness', 'readability'], 0.0)
    n = 0
    for r in results:
        gid = int(r.get('data_id', 0))
        rm = r.get('model', '')
        gt_md = gts.get(gid, {}).get('aggregated', {}).get(rm, {})
        gt_dims = gt_md.get('dimensions', {})
        jr = r.get('judge_result', {})
        if not jr:
            continue
        for d in sum_ae:
            j_score = dim_simple_avg(jr, d)
            g_score = gt_dims.get(d, None)
            if j_score is not None and g_score is not None:
                sum_ae[d] += abs(j_score - g_score / 10)
        n += 1
    print(f"  {model}: n={n}")
    for d in ['instruction_following', 'insight', 'comprehensiveness', 'readability']:
        print(f"    {d}: MAE={sum_ae[d]/n:.4f}")

# 2. Score Compression Table (vanilla mode)
print("\n" + "=" * 70)
print("2. Score Compression Table (vanilla mode)")
print("=" * 70)

for model in models_list:
    results = load_jsonl(BASE / f'outputs/judge_results/{model}/deepresearch_bench/vanilla.jsonl')
    j_scores, g_scores = [], []
    for r in results:
        gid = int(r.get('data_id', 0))
        rm = r.get('model', '')
        gt_md = gts.get(gid, {}).get('aggregated', {}).get(rm, {})
        gt_ov = gt_md.get('overall', None)
        jr = r.get('judge_result', {})
        j_ov = jr.get('overall_score', None)
        if j_ov is not None and gt_ov is not None:
            j_scores.append(float(j_ov))
            g_scores.append(gt_ov / 10)
    n = len(j_scores)
    jm = sum(j_scores) / n if n else 0
    gm = sum(g_scores) / n if n else 0
    js = (sum((s-jm)**2 for s in j_scores) / n) ** 0.5 if n else 0
    gs = (sum((s-gm)**2 for s in g_scores) / n) ** 0.5 if n else 0
    print(f"  {model}: n={n}, Judge μ={jm:.2f}, GT μ={gm:.2f}, Judge σ={js:.2f}, GT σ={gs:.2f}, Bias={jm-gm:+.2f}")

# Reference mode
print("\n  Reference mode:")
for model in ['gpt-4o-mini', 'deepseek-v4-flash', 'gpt-5.2']:
    results = load_jsonl(BASE / f'outputs/judge_results/{model}/deepresearch_bench/vanilla_reference.jsonl')
    j_scores = []
    for r in results:
        gid = int(r.get('data_id', 0))
        rm = r.get('model', '')
        gt_md = gts.get(gid, {}).get('aggregated', {}).get(rm, {})
        gt_ov = gt_md.get('overall', None)
        jr = r.get('judge_result', {})
        j_ov = jr.get('overall_score', None)
        if j_ov is not None and gt_ov is not None:
            j_scores.append(float(j_ov))
    n = len(j_scores)
    jm = sum(j_scores) / n if n else 0
    js = (sum((s-jm)**2 for s in j_scores) / n) ** 0.5 if n else 0
    print(f"  {model}: n={n}, Judge μ={jm:.2f}, Judge σ={js:.2f}")

# 3. Case Study specific values
print("\n" + "=" * 70)
print("3. Case Study specific verifications")
print("=" * 70)

# Case A1 (id=20, qwen3-max, gemini-2.5-pro-deepresearch)
gt20 = gts.get(20, {}).get('aggregated', {}).get('gemini-2.5-pro-deepresearch', {})
print(f"\nCase A1 GT: wt/10={gt20.get('weighted_total',0)/10:.2f}, IF/10={gt20.get('dimensions',{}).get('instruction_following',0)/10:.2f}, Comp/10={gt20.get('dimensions',{}).get('comprehensiveness',0)/10:.2f}")

# Case B1 (id=9, openai-deepresearch)
gt9 = gts.get(9, {}).get('aggregated', {}).get('openai-deepresearch', {})
print(f"Case B1 GT: wt/10={gt9.get('weighted_total',0)/10:.2f}, IF/10={gt9.get('dimensions',{}).get('instruction_following',0)/10:.2f}, Comp/10={gt9.get('dimensions',{}).get('comprehensiveness',0)/10:.2f}, Read/10={gt9.get('dimensions',{}).get('readability',0)/10:.2f}, Ins/10={gt9.get('dimensions',{}).get('insight',0)/10:.2f}")

# Case B2 (id=37)
gt37 = gts.get(37, {}).get('aggregated', {}).get('perplexity-Research', {})
print(f"Case B2 GT: overall/10={gt37.get('overall',0)/10:.2f}, Comp/10={gt37.get('dimensions',{}).get('comprehensiveness',0)/10:.2f}, Ins/10={gt37.get('dimensions',{}).get('insight',0)/10:.2f}")

# Pattern (c) id=2 GT
gt2 = gts.get(2, {}).get('aggregated', {}).get('perplexity-Research', {})
print(f"Pattern (c) GT: wt/10={gt2.get('weighted_total',0)/10:.2f}")

# Check judge values
print("\n  Judge values (rubric+reference mode):")
for did, model_name, mode_label, mode_file in [
    ('20', 'gemini-2.5-pro-deepresearch', 'Case A1 qwen3-max overall', 'qwen3-max'),
    ('9', 'openai-deepresearch', 'Case B1 qwen3-max overall', 'qwen3-max'),
    ('37', 'perplexity-Research', 'Case B2 qwen3-max overall', 'qwen3-max'),
]:
    results = load_jsonl(BASE / f'outputs/judge_results/{mode_file}/deepresearch_bench/vanilla_rubric_reference.jsonl')
    for r in results:
        if str(r.get('data_id')) == did and r.get('model') == model_name:
            jr = r.get('judge_result', {})
            weights = gts.get(int(did), {}).get('dimension_weights', {})
            # Weighted overall
            dim_scores = {}
            for d in ['instruction_following', 'comprehensiveness', 'readability', 'insight']:
                avg = dim_simple_avg(jr, d)
                if avg is not None:
                    dim_scores[d] = avg
            overall = None
            if dim_scores:
                total = sum(dim_scores.get(d, 0) * weights.get(d, 1.0) for d in dim_scores)
                w_sum = sum(weights.get(d, 1.0) for d in dim_scores)
                overall = total / w_sum if w_sum > 0 else None
            print(f"  {mode_label}: {overall:.4f}" if overall else f"  {mode_label}: N/A")
            break

print("\n  Judge values (plain rubric mode):")
for did, model_name, mode_label, mode_file in [
    ('2', 'perplexity-Research', 'Pattern (c) deepseek-v4-flash overall', 'deepseek-v4-flash'),
]:
    results = load_jsonl(BASE / f'outputs/judge_results/{mode_file}/deepresearch_bench/vanilla_rubric.jsonl')
    for r in results:
        if str(r.get('data_id')) == did and r.get('model') == model_name:
            jr = r.get('judge_result', {})
            weights = gts.get(int(did), {}).get('dimension_weights', {})
            dim_scores = {}
            for d in ['instruction_following', 'comprehensiveness', 'readability', 'insight']:
                avg = dim_simple_avg(jr, d)
                if avg is not None:
                    dim_scores[d] = avg
            overall = None
            if dim_scores:
                total = sum(dim_scores.get(d, 0) * weights.get(d, 1.0) for d in dim_scores)
                w_sum = sum(weights.get(d, 1.0) for d in dim_scores)
                overall = total / w_sum if w_sum > 0 else None
            print(f"  {mode_label}: {overall:.4f}" if overall else f"  {mode_label}: N/A")
            # Also print per-dimension avg
            print(f"    instruction_following avg={dim_scores.get('instruction_following', 'N/A')}")
            print(f"    comprehensiveness avg={dim_scores.get('comprehensiveness', 'N/A')}")
            print(f"    readability avg={dim_scores.get('readability', 'N/A')}")
            print(f"    insight avg={dim_scores.get('insight', 'N/A')}")
            break

# 4. Verify_bench_hard statistics
print("\n" + "=" * 70)
print("4. verify_bench_hard verification")
print("=" * 70)

vgt = load_jsonl(BASE / 'ground_truth' / 'verify_bench_hard_gt.jsonl')
vgt_map = {g['id']: g for g in vgt}
vdata = load_jsonl(BASE / 'data_standardized' / 'verify_bench_hard.jsonl')
vdata_at = {str(d['id']): d.get('ground_truth', {}).get('answer_type', 'unknown') for d in vdata}

# Per-case all-judges agreement
case_correct = {}
for model in models_list:
    results = load_jsonl(BASE / f'outputs/judge_results/{model}/verify_bench_hard/vanilla.jsonl')
    for r in results:
        did = r.get('data_id', '')
        if did not in case_correct:
            case_correct[did] = {}
        jv = str(r.get('judge_result', {}).get('verdict', '')).strip().upper()
        gv = vgt_map.get(did, {}).get('gold_correct', None)
        gs = 'YES' if gv is True else 'NO' if gv is False else '?'
        case_correct[did][model] = (jv == gs)

total = len(case_correct)
all_correct = sum(1 for m in case_correct.values() if all(v for v in m.values()))
all_wrong = sum(1 for m in case_correct.values() if not any(v for v in m.values()))
mixed = total - all_correct - all_wrong
print(f"  All judges correct: {all_correct}/{total} ({100*all_correct/total:.1f}%)")
print(f"  All judges wrong:   {all_wrong}/{total} ({100*all_wrong/total:.1f}%)")
print(f"  Mixed:              {mixed}/{total} ({100*mixed/total:.1f}%)")

# Per answer type: individual judge error rate
at_errors = Counter()
at_total = Counter()
for model in models_list:
    results = load_jsonl(BASE / f'outputs/judge_results/{model}/verify_bench_hard/vanilla.jsonl')
    for r in results:
        did = r.get('data_id', '')
        at = vdata_at.get(did, 'unknown')
        at_total[at] += 1
        jv = str(r.get('judge_result', {}).get('verdict', '')).strip().upper()
        gv = vgt_map.get(did, {}).get('gold_correct', None)
        gs = 'YES' if gv is True else 'NO' if gv is False else '?'
        if jv != gs:
            at_errors[at] += 1

print(f"\n  Per answer_type (individual judge error rate):")
for at in sorted(at_total.keys()):
    print(f"    {at}: {at_errors[at]}/{at_total[at]} ({100*at_errors[at]/at_total[at]:.1f}%)")

print("\n  Verification complete.")
