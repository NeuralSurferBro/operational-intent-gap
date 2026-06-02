from examples.fraud_dispute_demo import control_aware_agent_execution, shortcut_agent_execution
from oig import fraud_dispute_workflow, score_execution


def test_shortcut_agent_has_large_operational_intent_gap():
    workflow = fraud_dispute_workflow()
    score = score_execution(workflow, shortcut_agent_execution())

    assert score.task_completion == 1.0
    assert score.operational_intent_gap > 0.75
    assert len(score.violations) >= 4


def test_control_aware_agent_preserves_operational_intent():
    workflow = fraud_dispute_workflow()
    score = score_execution(workflow, control_aware_agent_execution())

    assert score.task_completion == 1.0
    assert score.operational_intent_preservation > 0.95
    assert score.operational_intent_gap < 0.05
    assert score.violations == []
