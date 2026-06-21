from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
import math
import random
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class LearningAuditConfig:
    seed: int = 2026
    n: int = 360
    test_fraction: float = 0.30
    supervised_threshold: float = 0.55
    cluster_count: int = 3
    bandit_rounds: int = 240
    epsilon: float = 0.12


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = sorted({key for row in rows for key in row})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def generate_synthetic_observations(config: LearningAuditConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    centers = [(0.22, 0.70), (0.65, 0.58), (0.55, 0.22)]
    rows: list[dict[str, object]] = []
    for unit_id in range(1, config.n + 1):
        latent_group = (unit_id - 1) % len(centers)
        cx, cy = centers[latent_group]
        x1 = max(0.0, min(1.0, rng.gauss(cx, 0.11)))
        x2 = max(0.0, min(1.0, rng.gauss(cy, 0.12)))
        institutional_noise = rng.gauss(0.0, 0.10)
        score_true = sigmoid(-0.55 + 1.55 * x1 - 1.05 * x2 + 0.35 * latent_group + institutional_noise)
        label = 1 if rng.random() < score_true else 0
        split = "test" if rng.random() < config.test_fraction else "train"
        rows.append({
            "unit_id": unit_id,
            "feature_access": round(x1, 6),
            "feature_risk": round(x2, 6),
            "latent_group": latent_group,
            "true_probability": round(score_true, 6),
            "label": label,
            "split": split,
            "interpretation": "Synthetic features support supervised labels, unsupervised clusters, and governance review of measurement assumptions.",
        })
    return rows


def fit_supervised_score(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    scored: list[dict[str, object]] = []
    for row in rows:
        score = sigmoid(-0.70 + 1.75 * float(row["feature_access"]) - 1.10 * float(row["feature_risk"]))
        new_row = dict(row)
        new_row["predicted_probability"] = round(score, 6)
        scored.append(new_row)
    return scored


def supervised_metrics(rows: list[dict[str, object]], threshold: float) -> list[dict[str, object]]:
    metrics: list[dict[str, object]] = []
    for split in ["train", "test", "all"]:
        subset = rows if split == "all" else [row for row in rows if row["split"] == split]
        tp = fp = tn = fn = 0
        for row in subset:
            pred = 1 if float(row["predicted_probability"]) >= threshold else 0
            label = int(row["label"])
            if pred == 1 and label == 1: tp += 1
            elif pred == 1 and label == 0: fp += 1
            elif pred == 0 and label == 0: tn += 1
            else: fn += 1
        total = max(1, len(subset))
        accuracy = (tp + tn) / total
        precision = tp / max(1, tp + fp)
        recall = tp / max(1, tp + fn)
        f1 = 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)
        metrics.append({
            "paradigm": "supervised_learning",
            "split": split,
            "threshold": threshold,
            "n": len(subset),
            "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "accuracy": round(accuracy, 6),
            "precision": round(precision, 6),
            "recall": round(recall, 6),
            "f1": round(f1, 6),
            "interpretation": "Classification metrics depend on labels, threshold choice, split integrity, and intended use.",
        })
    return metrics


def nearest_center(row: dict[str, object], centers: list[tuple[float, float]]) -> int:
    x, y = float(row["feature_access"]), float(row["feature_risk"])
    distances = [((x - cx) ** 2 + (y - cy) ** 2, idx) for idx, (cx, cy) in enumerate(centers)]
    return min(distances)[1]


def simple_kmeans(rows: list[dict[str, object]], k: int, rounds: int = 8) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    centers = [(0.20, 0.75), (0.65, 0.55), (0.55, 0.20)][:k]
    assignments: list[int] = []
    for _ in range(rounds):
        assignments = [nearest_center(row, centers) for row in rows]
        new_centers: list[tuple[float, float]] = []
        for cluster in range(k):
            members = [row for row, assigned in zip(rows, assignments) if assigned == cluster]
            if members:
                new_centers.append((mean(float(row["feature_access"]) for row in members), mean(float(row["feature_risk"]) for row in members)))
            else:
                new_centers.append(centers[cluster])
        centers = new_centers
    assignment_rows: list[dict[str, object]] = []
    for row, cluster in zip(rows, assignments):
        cx, cy = centers[cluster]
        distance = math.sqrt((float(row["feature_access"]) - cx) ** 2 + (float(row["feature_risk"]) - cy) ** 2)
        assignment_rows.append({
            "unit_id": row["unit_id"],
            "cluster": cluster,
            "latent_group": row["latent_group"],
            "feature_access": row["feature_access"],
            "feature_risk": row["feature_risk"],
            "distance_to_centroid": round(distance, 6),
            "interpretation": "Unsupervised cluster assignment is a pattern summary, not a discovered social identity or causal explanation.",
        })
    summary_rows: list[dict[str, object]] = []
    for cluster in range(k):
        members = [row for row in assignment_rows if int(row["cluster"]) == cluster]
        cx, cy = centers[cluster]
        summary_rows.append({
            "paradigm": "unsupervised_learning",
            "cluster": cluster,
            "n": len(members),
            "centroid_access": round(cx, 6),
            "centroid_risk": round(cy, 6),
            "mean_distance_to_centroid": round(mean(float(row["distance_to_centroid"]) for row in members), 6) if members else None,
            "interpretation": "Clusters require interpretation, validation, and caution before institutional use.",
        })
    return assignment_rows, summary_rows


def reinforcement_learning_trace(config: LearningAuditConfig) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rng = random.Random(config.seed + 17)
    arms = [
        {"arm": "baseline", "reward_probability": 0.42},
        {"arm": "support", "reward_probability": 0.54},
        {"arm": "intensive_support", "reward_probability": 0.49},
    ]
    counts = {arm["arm"]: 0 for arm in arms}
    rewards = {arm["arm"]: 0.0 for arm in arms}
    rows: list[dict[str, object]] = []
    for step in range(1, config.bandit_rounds + 1):
        if rng.random() < config.epsilon or all(count == 0 for count in counts.values()):
            chosen = rng.choice(arms)
            decision_rule = "explore"
        else:
            chosen_name = max(counts, key=lambda name: rewards[name] / max(1, counts[name]))
            chosen = next(arm for arm in arms if arm["arm"] == chosen_name)
            decision_rule = "exploit"
        reward = 1 if rng.random() < float(chosen["reward_probability"]) else 0
        counts[chosen["arm"]] += 1
        rewards[chosen["arm"]] += reward
        rows.append({
            "paradigm": "reinforcement_learning",
            "step": step,
            "arm": chosen["arm"],
            "decision_rule": decision_rule,
            "reward": reward,
            "running_average_reward": round(sum(rewards.values()) / step, 6),
            "interpretation": "Reward feedback updates future action; safe deployment requires reward review and exploration boundaries.",
        })
    summary = []
    for arm in arms:
        name = str(arm["arm"])
        summary.append({
            "paradigm": "reinforcement_learning",
            "arm": name,
            "true_reward_probability": arm["reward_probability"],
            "times_selected": counts[name],
            "observed_mean_reward": round(rewards[name] / max(1, counts[name]), 6),
            "interpretation": "Observed reward estimates are feedback records, not proof that the reward captures the right institutional goal.",
        })
    return rows, summary


def governance_register() -> list[dict[str, object]]:
    return [
        {"paradigm": "supervised_learning", "governance_item": "label_validity", "review_question": "Do labels measure the intended outcome rather than institutional convenience?", "status": "needs_review"},
        {"paradigm": "supervised_learning", "governance_item": "generalization", "review_question": "Does the model perform beyond the training set and across relevant subgroups?", "status": "partial"},
        {"paradigm": "unsupervised_learning", "governance_item": "cluster_interpretation", "review_question": "Are clusters interpreted cautiously and validated against domain knowledge?", "status": "needs_review"},
        {"paradigm": "unsupervised_learning", "governance_item": "feature_scaling", "review_question": "Do distance calculations depend on arbitrary feature scaling?", "status": "complete"},
        {"paradigm": "reinforcement_learning", "governance_item": "reward_alignment", "review_question": "Does the reward function reflect the actual public or institutional purpose?", "status": "needs_review"},
        {"paradigm": "reinforcement_learning", "governance_item": "exploration_safety", "review_question": "Are exploration and experimentation bounded in high-stakes settings?", "status": "needs_review"},
    ]


def main() -> None:
    config = LearningAuditConfig()
    observations = fit_supervised_score(generate_synthetic_observations(config))
    supervised = supervised_metrics(observations, config.supervised_threshold)
    cluster_assignments, cluster_summary = simple_kmeans(observations, config.cluster_count)
    rl_trace, rl_summary = reinforcement_learning_trace(config)
    governance = governance_register()
    train_acc = next(row for row in supervised if row["split"] == "train")["accuracy"]
    test_acc = next(row for row in supervised if row["split"] == "test")["accuracy"]
    summary = {
        "article": "supervised_unsupervised_and_reinforcement_learning",
        "timestamp_utc": timestamp_utc(),
        "n_observations": config.n,
        "supervised_test_accuracy": test_acc,
        "supervised_generalization_gap": round(float(train_acc) - float(test_acc), 6),
        "cluster_count": config.cluster_count,
        "rl_rounds": config.bandit_rounds,
        "rl_final_average_reward": rl_trace[-1]["running_average_reward"],
        "governance_items_needing_review": sum(1 for row in governance if row["status"] == "needs_review"),
        "interpretation": "Learning paradigms differ in evidence structure: supervised learning uses labels, unsupervised learning searches for structure, and reinforcement learning updates action from rewards.",
    }
    write_csv(TABLES / "supervised_observations.csv", observations)
    write_csv(TABLES / "supervised_metrics.csv", supervised)
    write_csv(TABLES / "unsupervised_cluster_assignments.csv", cluster_assignments)
    write_csv(TABLES / "unsupervised_cluster_summary.csv", cluster_summary)
    write_csv(TABLES / "reinforcement_learning_trace.csv", rl_trace)
    write_csv(TABLES / "reinforcement_learning_summary.csv", rl_summary)
    write_csv(TABLES / "learning_paradigm_governance_register.csv", governance)
    write_json(JSON_DIR / "learning_audit_config.json", asdict(config))
    write_json(JSON_DIR / "learning_paradigms_audit_summary.json", summary)
    write_json(JSON_DIR / "supervised_metrics.json", supervised)
    write_json(JSON_DIR / "unsupervised_cluster_summary.json", cluster_summary)
    write_json(JSON_DIR / "reinforcement_learning_summary.json", rl_summary)
    print("Learning paradigms audit complete.")
    print(TABLES / "supervised_metrics.csv")


if __name__ == "__main__":
    main()
