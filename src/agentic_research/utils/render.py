from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def render_markdown(plan_data: dict, output_path: str) -> None:
    """
    Render experiment plan to a markdown file using Jinja2 template.
    """

    templates_dir = Path("templates/experiment_templates")

    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = env.get_template("experiment.md.j2")

    rendered = template.render(**plan_data)

    with open(output_path, "w") as f:
        f.write(rendered)

