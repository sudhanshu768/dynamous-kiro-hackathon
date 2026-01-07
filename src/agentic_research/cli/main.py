import click

from agentic_research.cli.commands.plan import plan


@click.group()
def cli():
    """Agentic Research Engineer CLI."""
    pass


cli.add_command(plan)


if __name__ == "__main__":
    cli()

