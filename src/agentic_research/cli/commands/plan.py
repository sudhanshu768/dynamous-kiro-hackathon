import click
from pathlib import Path

from agentic_research.core.planner import ExperimentPlanner
from agentic_research.utils.render import render_experiment_plan


@click.command(help="Generate an experiment plan.")
@click.option("--problem", required=True, help="Research problem statement")
@click.option("--dataset", help="Dataset description")
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    help="Output markdown file (e.g. plan.md)",
)
def plan(problem: str, dataset: str | None, output: Path | None):
    planner = ExperimentPlanner()
    plan_data = planner.generate_plan(problem, dataset)

    if output:
        render_experiment_plan(plan_data, output)
        click.echo(f" Experiment plan written to {output}")
    else:
        click.echo("\n Experiment Plan (Preview)\n")
        for k, v in plan_data.items():
            click.echo(f"{k}: {v}")

