"""
Core experiment planning logic (Phase 7A).
Deterministic fallback + optional AI-assisted hypothesis.
"""

from typing import Dict, List, Optional


class ExperimentPlanner:
    def generate_plan(
        self,
        problem: str,
        dataset: Optional[str] = None,
        ai_hypothesis: Optional[str] = None,
    ) -> Dict:
        """
        Entry point for experiment planning.

        If ai_hypothesis is provided → AI-assisted mode
        Else → deterministic fallback
        """

        if ai_hypothesis:
            return self._generate_with_ai(problem, dataset, ai_hypothesis)

        return self._generate_deterministic(problem, dataset)

    # --------------------------------------------------
    # Deterministic fallback (Phase 4)
    # --------------------------------------------------
    def _generate_deterministic(
        self,
        problem: str,
        dataset: Optional[str],
    ) -> Dict:
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
            "notes": "Deterministic fallback (Phase 4)",
        }

    # --------------------------------------------------
    # AI-assisted mode (Kiro, Phase 7A)
    # --------------------------------------------------
    def _generate_with_ai(
        self,
        problem: str,
        dataset: Optional[str],
        hypothesis: str,
    ) -> Dict:
        return {
            "problem": problem,
            "dataset": dataset,
            "hypothesis": hypothesis,
            "baselines": [
                "Rule-based heuristic",
                "Simple ML baseline",
            ],
            "metrics": [
                "Accuracy",
                "Precision",
                "Recall",
            ],
            "notes": "AI-assisted hypothesis (Kiro, Phase 7A)",
        }

