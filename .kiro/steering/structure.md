# Project Structure

## Directory Layout
```
agentic-research-engineer/
├── src/
│   ├── agentic_research/
│   │   ├── __init__.py
│   │   ├── cli/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── commands/
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── planner.py
│   │   │   ├── templates.py
│   │   │   └── validator.py
│   │   ├── integrations/
│   │   │   ├── __init__.py
│   │   │   ├── mlflow_integration.py
│   │   │   ├── wandb_integration.py
│   │   │   └── framework_adapters.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── config.py
│   │       └── helpers.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/
│   ├── user_guide/
│   ├── api_reference/
│   └── examples/
├── templates/
│   ├── experiment_templates/
│   ├── documentation_templates/
│   └── config_templates/
├── examples/
│   ├── computer_vision/
│   ├── nlp/
│   └── reinforcement_learning/
├── pyproject.toml
├── requirements.txt
├── README.md
├── CHANGELOG.md
└── .kiro/
```

## File Naming Conventions
- **Python modules**: snake_case (e.g., `experiment_planner.py`)
- **Classes**: PascalCase (e.g., `ExperimentPlanner`)
- **Functions/variables**: snake_case (e.g., `generate_plan`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_CONFIG_PATH`)
- **Test files**: `test_*.py` or `*_test.py`
- **Configuration files**: lowercase with extensions (e.g., `config.yaml`)

## Module Organization
- **CLI Layer**: Command-line interface and argument parsing
- **Core Logic**: Main business logic for experiment planning and validation
- **Integrations**: External service and framework integrations
- **Utils**: Shared utilities, configuration management, and helpers
- **Templates**: Reusable templates for experiments and documentation

## Configuration Files
- **pyproject.toml**: Project metadata, dependencies, and build configuration
- **requirements.txt**: Python dependencies for pip users
- **.kiro/**: Kiro CLI configuration and steering documents
- **config/**: User configuration templates and defaults
- **templates/**: Experiment and documentation templates

## Documentation Structure
- **User Guide**: Installation, quickstart, and usage tutorials
- **API Reference**: Auto-generated API documentation
- **Examples**: Real-world usage examples by ML domain
- **Contributing**: Development setup and contribution guidelines

## Asset Organization
- **templates/**: Jinja2 templates for experiment generation
- **examples/**: Sample experiment configurations and outputs
- **docs/assets/**: Documentation images and diagrams
- **tests/fixtures/**: Test data and mock configurations

## Build Artifacts
- **dist/**: Built packages for PyPI distribution
- **build/**: Temporary build files
- **.pytest_cache/**: Pytest cache files
- **__pycache__/**: Python bytecode cache
- **.coverage**: Test coverage reports

## Environment-Specific Files
- **.env**: Local environment variables (not committed)
- **config/dev.yaml**: Development configuration
- **config/prod.yaml**: Production configuration
- **docker/**: Docker configurations for different environments
