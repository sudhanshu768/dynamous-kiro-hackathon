"""
Markdown rendering utilities for experiment plans.
"""

from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def render_markdown(plan_data: dict, output_path: str) -> None:
    """
    Render an experiment plan to a markdown file using Jinja2 template.
    """

    template_dir = Path("templates/experiment_templates")
    env = Environment(loader=FileSystemLoader(template_dir))

    template = env.get_template("experiment.md.j2")

    rendered = template.render(plan=plan_data)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)

