"""
Core experiment planning logic (Phase 4).
Deterministic, no AI calls yet.
"""

from typing import Dict, List, Optional


class ExperimentPlanner:
    def generate_plan(
        self,
        problem: str,
        dataset: Optional[str] = None,
    ) -> Dict:
        """
        Generate a deterministic experiment plan (Phase 4).
        """

        hypothesis = (
            f"If we apply machine learning techniques to '{problem}', "
            "we expect measurable improvement over naive baselines."
        )

        baselines: List[str] = [
            "Majority class",
            "Simple heuristic",
        ]

        metrics: List[str] = [
            "Accuracy",
            "Precision",
            "Recall",
        ]

        return {
            "problem": problem,
            "dataset": dataset,
            "hypothesis": hypothesis,
            "baselines": baselines,
            "metrics": metrics,
            "notes": "Deterministic hypothesis generation (Phase 4)",
        }

