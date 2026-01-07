import click


@click.command()
@click.option("--problem", required=True, help="Research problem statement")
@click.option("--dataset", required=False, help="Dataset description")
def plan(problem: str, dataset: str | None):
    """
    Phase 2 stub for experiment planning.
    """
    click.echo("📌 Plan command invoked")
    click.echo(f"Problem: {problem}")
    click.echo(f"Dataset: {dataset}")

