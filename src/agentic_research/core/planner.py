class ExperimentPlanner:
    def __init__(self):
        pass

    def generate_plan(self, problem: str, dataset: str | None = None) -> dict:
        hypothesis = (
            f"If we apply machine learning techniques to '{problem}', "
            f"we expect measurable improvement over naive baselines."
        )

        return {
            "problem": problem,
            "dataset": dataset,
            "hypothesis": hypothesis,
            "baselines": ["Majority class", "Simple heuristic"],
            "metrics": ["Accuracy", "Precision", "Recall"],
            "notes": "Deterministic hypothesis generation (Phase 4.2)",
        }

