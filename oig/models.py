from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass(frozen=True)
class Step:
    """A required operational step in a regulated workflow."""

    name: str
    description: str
    required_artifact: Optional[str] = None
    required: bool = True


@dataclass(frozen=True)
class Constraint:
    """A hard control that must be satisfied for intent preservation."""

    name: str
    description: str
    required_step: Optional[str] = None
    required_artifact: Optional[str] = None
    severity: Severity = Severity.CRITICAL


@dataclass
class Workflow:
    """A banking workflow encoded as steps plus controls."""

    name: str
    intent: str
    steps: List[Step]
    constraints: List[Constraint]


@dataclass
class AgentExecution:
    """What an agent actually did."""

    workflow_name: str
    completed: bool
    completed_steps: List[str]
    artifacts: Dict[str, str] = field(default_factory=dict)
    resolution_minutes: int = 0
    decision: Optional[str] = None
    customer_harm_score: float = 0.0  # 0.0=no harm, 1.0=max harm
    notes: List[str] = field(default_factory=list)


@dataclass
class ScoreBreakdown:
    task_completion: float
    control_adherence: float
    auditability: float
    harm_minimization: float
    operational_intent_preservation: float
    operational_intent_gap: float
    violations: List[str]
