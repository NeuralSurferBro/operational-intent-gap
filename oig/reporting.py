from __future__ import annotations

from .models import AgentExecution, ScoreBreakdown


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def print_report(label: str, execution: AgentExecution, score: ScoreBreakdown) -> None:
    print("=" * 72)
    print(label)
    print("=" * 72)
    print(f"Decision: {execution.decision}")
    print(f"Resolution Time: {execution.resolution_minutes} minutes")
    print(f"Task Completion: {pct(score.task_completion)}")
    print(f"Control Adherence: {pct(score.control_adherence)}")
    print(f"Auditability: {pct(score.auditability)}")
    print(f"Harm Minimization: {pct(score.harm_minimization)}")
    print(f"Operational Intent Preservation: {pct(score.operational_intent_preservation)}")
    print(f"Operational Intent Gap: {pct(score.operational_intent_gap)}")
    if score.violations:
        print("\nViolations:")
        for violation in score.violations:
            print(f"- {violation}")
    print()
