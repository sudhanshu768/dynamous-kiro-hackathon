import click

from agentic_research.core.planner import ExperimentPlanner
from agentic_research.core.validator import validate_inputs


@click.command(help="Generate a research experiment plan.")
@click.option("--problem", required=True, help="Research problem statement")
@click.option("--dataset", help="Dataset description")
@click.option("--output", help="Write plan to markdown file")
def plan(problem, dataset, output):
    # 🔎 Validation
    validation = validate_inputs(problem, dataset)

    for warning in validation.warnings:
        click.echo(f"  Warning: {warning}")

    if validation.has_errors():
        for error in validation.errors:
            click.echo(f" Error: {error}")
        raise SystemExit(1)

    #  Planning
    planner = ExperimentPlanner()
    plan_data = planner.generate_plan(problem, dataset)

    #  Output
    if output:
        from agentic_research.utils.render import render_markdown

        render_markdown(plan_data, output)
        click.echo(f"\n Experiment plan written to {output}")
    else:
        click.echo("\n Experiment Plan")
        click.echo("-" * 30)
        for k, v in plan_data.items():
            click.echo(f"{k}: {v}")

