from algorithms_computational_reasoning.cli import complexity_demo


def test_complexity_demo_has_n_values():
    result = complexity_demo()
    assert "n" in result
    assert len(result["n"]) == 4
