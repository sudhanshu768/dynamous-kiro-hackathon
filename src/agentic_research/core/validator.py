"""
Validation logic for experiment planning (Phase 7A).
"""

from typing import List, Optional


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def has_errors(self) -> bool:
        return len(self.errors) > 0


def validate_inputs(problem: str, dataset: Optional[str]) -> ValidationResult:
    """
    Validate CLI inputs before experiment planning.
    """
    result = ValidationResult()

    # Hard validation
    if not problem or not problem.strip():
        result.errors.append("Problem statement cannot be empty.")

    if len(problem.strip()) < 5:
        result.errors.append("Problem statement is too short.")

    # Soft warnings
    if not dataset:
        result.warnings.append("Dataset not provided. Plan may be incomplete.")

    return result

