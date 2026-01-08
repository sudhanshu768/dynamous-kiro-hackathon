from agentic_research.core.planner import ExperimentPlanner
import click

@click.command()
@click.option("--problem", required=True, help="Research problem statement")
@click.option("--dataset", help="Dataset description")
def plan(problem, dataset):
    planner = ExperimentPlanner()
    plan = planner.generate_plan(problem, dataset)

    click.echo("\n  Experiment Plan (Phase 4.2)")
    click.echo("-" * 30)
    for k, v in plan.items():
        click.echo(f"{k}: {v}")

