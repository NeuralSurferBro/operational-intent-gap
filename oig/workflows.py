from __future__ import annotations

from .models import Constraint, Severity, Step, Workflow


def fraud_dispute_workflow() -> Workflow:
    """A simplified fraud dispute workflow for demonstration only.

    This is not legal, regulatory, or operational advice. It is a toy workflow
    designed to demonstrate the Operational Intent Gap concept.
    """

    return Workflow(
        name="fraud_dispute",
        intent=(
            "Resolve a customer fraud dispute while preserving customer protection, "
            "evidence review, regulatory checkpoints, auditability, and escalation discipline."
        ),
        steps=[
            Step("verify_identity", "Verify the customer before working the case.", "identity_verification"),
            Step("collect_evidence", "Collect transaction and customer evidence.", "evidence_packet"),
            Step("policy_review", "Apply the institution's fraud policy.", "policy_review_notes"),
            Step("regulatory_check", "Check applicable dispute timing and notice obligations.", "regulatory_checklist"),
            Step("decision", "Make and document a case decision.", "decision_rationale"),
            Step("customer_notice", "Notify the customer of the decision and next steps.", "customer_notice"),
        ],
        constraints=[
            Constraint(
                "identity-before-decision",
                "A decision cannot be made before identity verification.",
                required_step="verify_identity",
                required_artifact="identity_verification",
            ),
            Constraint(
                "evidence-before-denial",
                "A denial requires evidence review and a documented rationale.",
                required_step="collect_evidence",
                required_artifact="evidence_packet",
            ),
            Constraint(
                "policy-rationale-required",
                "Decision must reference policy basis.",
                required_step="policy_review",
                required_artifact="policy_review_notes",
            ),
            Constraint(
                "regulatory-checkpoint-required",
                "Regulatory timing and notice checks must be documented.",
                required_step="regulatory_check",
                required_artifact="regulatory_checklist",
            ),
            Constraint(
                "customer-notice-required",
                "The customer must receive a documented notice.",
                required_step="customer_notice",
                required_artifact="customer_notice",
                severity=Severity.WARNING,
            ),
        ],
    )
