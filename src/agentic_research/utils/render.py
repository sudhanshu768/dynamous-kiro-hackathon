"""
Render experiment plans to Markdown using Jinja2.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def render_experiment_plan(plan: dict, output_path: Path) -> None:
    """
    Render experiment plan dictionary into a markdown file.
    """

    env = Environment(
        loader=FileSystemLoader("templates/experiment_templates"),
        autoescape=False,
    )

    template = env.get_template("experiment.md.j2")
    rendered = template.render(**plan)

    output_path.write_text(rendered, encoding="utf-8")

