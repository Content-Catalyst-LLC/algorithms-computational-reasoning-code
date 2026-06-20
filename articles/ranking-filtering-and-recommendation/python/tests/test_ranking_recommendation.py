from ranking_recommendation.audit import cosine_similarity, rank_candidates, score_candidate


def test_cosine_similarity_is_bounded():
    value = cosine_similarity([1.0, 0.0], [1.0, 1.0])
    assert 0.0 <= value <= 1.0


def test_filter_removes_ineligible_candidate():
    candidates = [
        {"candidate_id": "A", "eligible": True, "text_match": 1, "quality": 1, "freshness": 1, "diversity_bonus": 0, "risk_penalty": 0},
        {"candidate_id": "B", "eligible": False, "text_match": 1, "quality": 1, "freshness": 1, "diversity_bonus": 0, "risk_penalty": 0},
    ]
    weights = {"text_match": 0.3, "quality": 0.3, "freshness": 0.2, "diversity_bonus": 0.1, "risk_penalty": 0.1}
    ranked = rank_candidates(candidates, weights)
    assert [row["candidate_id"] for row in ranked] == ["A"]


def test_risk_penalty_lowers_score():
    base = {"text_match": 0.8, "quality": 0.8, "freshness": 0.8, "diversity_bonus": 0.2, "risk_penalty": 0.0}
    risky = {**base, "risk_penalty": 0.9}
    weights = {"text_match": 0.36, "quality": 0.30, "freshness": 0.16, "diversity_bonus": 0.14, "risk_penalty": 0.20}
    assert score_candidate(base, weights) > score_candidate(risky, weights)
