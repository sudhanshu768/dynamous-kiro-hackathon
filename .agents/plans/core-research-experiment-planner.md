# Feature: Core Research Experiment Planning Agent

The following plan should be complete, but it's important that you validate documentation and codebase patterns and task sanity before you start implementing.

Pay special attention to naming of existing utils types and models. Import from the right files etc.

## Feature Description

Implement the core research experiment planning agent that accepts research problem statements and dataset descriptions via CLI and generates comprehensive, structured experiment plans. The agent focuses on research rigor, explainability, and reproducibility by producing detailed plans with clear hypotheses, justified baseline selections, appropriate evaluation metrics, step-by-step procedures, and reproducibility checks. This is the foundational feature that transforms vague research ideas into actionable, scientifically sound experiment designs.

## User Story

As a machine learning researcher
I want to input a research problem statement and dataset description via CLI
So that I can receive a comprehensive, structured experiment plan with clear hypotheses, baselines, metrics, and reproducibility guidelines that ensures rigorous scientific methodology

## Problem Statement

ML researchers often struggle to convert abstract research ideas into structured, reproducible experiment plans. Current tools focus on automated model training rather than the critical planning phase that ensures scientific rigor. Researchers need assistance in formulating clear hypotheses, selecting appropriate baselines, choosing justified evaluation metrics, and establishing reproducibility standards before any code is written.

## Solution Statement

Create a CLI-based research experiment planning agent that uses AI to analyze research problems and datasets, then generates comprehensive experiment plans following established ML research methodology. The agent will guide researchers through hypothesis formulation, baseline selection, metric justification, and reproducibility planning, producing structured markdown documents that serve as implementation blueprints.

## Feature Metadata

**Feature Type**: New Capability
**Estimated Complexity**: High
**Primary Systems Affected**: CLI interface, Core planning logic, Template engine, AI integration
**Dependencies**: Click/Typer CLI framework, OpenAI/Anthropic APIs, Jinja2 templates, YAML configuration

---

## CONTEXT REFERENCES

### Relevant Codebase Files IMPORTANT: YOU MUST READ THESE FILES BEFORE IMPLEMENTING!

- `.kiro/steering/structure.md` - Why: Defines project structure and module organization patterns
- `.kiro/steering/tech.md` - Why: Specifies technology stack, CLI framework choice, and coding standards
- `.kiro/steering/product.md` - Why: Contains product vision and user journey for experiment planning

### New Files to Create

- `src/agentic_research/__init__.py` - Package initialization
- `src/agentic_research/cli/__init__.py` - CLI package initialization
- `src/agentic_research/cli/main.py` - Main CLI entry point with Click group
- `src/agentic_research/cli/commands/__init__.py` - Commands package initialization
- `src/agentic_research/cli/commands/plan.py` - Plan command implementation
- `src/agentic_research/core/__init__.py` - Core package initialization
- `src/agentic_research/core/planner.py` - Main experiment planning logic
- `src/agentic_research/core/templates.py` - Template management and rendering
- `src/agentic_research/core/validator.py` - Plan validation logic
- `src/agentic_research/utils/__init__.py` - Utils package initialization
- `src/agentic_research/utils/config.py` - Configuration management
- `src/agentic_research/utils/helpers.py` - Utility functions
- `templates/experiment_templates/research_plan.md.j2` - Jinja2 template for experiment plans
- `pyproject.toml` - Project configuration and dependencies
- `tests/unit/test_planner.py` - Unit tests for planner
- `tests/unit/test_cli.py` - Unit tests for CLI commands
- `tests/integration/test_plan_generation.py` - Integration tests

### Relevant Documentation YOU SHOULD READ THESE BEFORE IMPLEMENTING!

- [Click Commands and Groups Documentation](https://click.palletsprojects.com/en/8.0.x/commands/)
  - Specific section: Command groups and subcommands
  - Why: Required for implementing CLI structure with plan subcommand
- [Google ML Experiments Best Practices](https://developers.google.com/machine-learning/managing-ml-projects/experiments)
  - Specific section: Baseline performance and experimental methodology
  - Why: Provides framework for experiment planning methodology
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/)
  - Specific section: Template syntax and rendering
  - Why: Needed for generating structured experiment plan documents

### Patterns to Follow

**Naming Conventions:**
- Python modules: snake_case (e.g., `experiment_planner.py`)
- Classes: PascalCase (e.g., `ExperimentPlanner`)
- Functions/variables: snake_case (e.g., `generate_plan`)
- Constants: UPPER_SNAKE_CASE (e.g., `DEFAULT_CONFIG_PATH`)

**Error Handling:**
- Explicit exception handling with informative messages
- Custom exception classes for domain-specific errors
- Graceful degradation for AI API failures

**Logging Pattern:**
- Use Python logging module with structured logging
- Log levels: DEBUG for detailed flow, INFO for user actions, ERROR for failures
- Include context information in log messages

**CLI Pattern:**
- Use Click groups for command organization
- Implement `--help` for all commands with clear descriptions
- Use Click options with proper validation and defaults
- Follow Click's parameter separation between commands and subcommands

---

## IMPLEMENTATION PLAN

### Phase 1: Foundation

Set up the basic project structure, configuration management, and CLI framework foundation before implementing core planning logic.

**Tasks:**
- Create Python package structure following steering document specifications
- Set up pyproject.toml with dependencies (Click, Jinja2, OpenAI/Anthropic clients)
- Implement configuration management for API keys and user preferences
- Create basic CLI entry point with Click group structure

### Phase 2: Core Implementation

Implement the main experiment planning logic, AI integration, and template rendering system.

**Tasks:**
- Develop ExperimentPlanner class with AI-powered analysis capabilities
- Implement research problem analysis and hypothesis generation
- Create baseline selection and evaluation metrics recommendation logic
- Build template rendering system for structured plan output

### Phase 3: Integration

Connect CLI interface with core planning logic and implement the complete user workflow.

**Tasks:**
- Implement plan command with proper argument parsing and validation
- Integrate AI services with error handling and fallback mechanisms
- Connect template engine with planner output
- Add configuration file support for user preferences

### Phase 4: Testing & Validation

Implement comprehensive testing and validation to ensure reliability and correctness.

**Tasks:**
- Create unit tests for all core components
- Implement integration tests for end-to-end workflow
- Add validation for generated plans against research methodology standards
- Test CLI interface with various input scenarios

---

## STEP-BY-STEP TASKS

IMPORTANT: Execute every task in order, top to bottom. Each task is atomic and independently testable.

### CREATE pyproject.toml

- **IMPLEMENT**: Project metadata, dependencies, and build configuration
- **PATTERN**: Standard Python packaging with Poetry-style configuration
- **IMPORTS**: click>=8.0.0, jinja2>=3.1.0, openai>=1.0.0, anthropic>=0.8.0, pyyaml>=6.0, pydantic>=2.0.0
- **GOTCHA**: Pin major versions to avoid breaking changes
- **VALIDATE**: `python -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))"`

### CREATE src/agentic_research/__init__.py

- **IMPLEMENT**: Package initialization with version info
- **PATTERN**: Standard Python package init with __version__ export
- **IMPORTS**: None required for basic init
- **GOTCHA**: Keep minimal to avoid circular imports
- **VALIDATE**: `python -c "import src.agentic_research; print(src.agentic_research.__version__)"`

### CREATE src/agentic_research/utils/__init__.py

- **IMPLEMENT**: Utils package initialization
- **PATTERN**: Empty init file for package recognition
- **IMPORTS**: None
- **GOTCHA**: None
- **VALIDATE**: `python -c "import src.agentic_research.utils"`

### CREATE src/agentic_research/utils/config.py

- **IMPLEMENT**: Configuration management with environment variables and file support
- **PATTERN**: Pydantic BaseSettings for configuration validation
- **IMPORTS**: pydantic.BaseSettings, os, pathlib, yaml
- **GOTCHA**: Handle missing API keys gracefully with clear error messages
- **VALIDATE**: `python -c "from src.agentic_research.utils.config import Config; c = Config()"`

### CREATE src/agentic_research/utils/helpers.py

- **IMPLEMENT**: Utility functions for file operations and text processing
- **PATTERN**: Pure functions with type hints and docstrings
- **IMPORTS**: pathlib, typing, re
- **GOTCHA**: Handle file permissions and encoding issues
- **VALIDATE**: `python -c "from src.agentic_research.utils.helpers import *"`

### CREATE src/agentic_research/core/__init__.py

- **IMPLEMENT**: Core package initialization
- **PATTERN**: Empty init file for package recognition
- **IMPORTS**: None
- **GOTCHA**: None
- **VALIDATE**: `python -c "import src.agentic_research.core"`

### CREATE templates/experiment_templates/research_plan.md.j2

- **IMPLEMENT**: Jinja2 template for structured experiment plan output
- **PATTERN**: Markdown template with Jinja2 variables and loops
- **IMPORTS**: None (template file)
- **GOTCHA**: Ensure proper escaping of user input in template
- **VALIDATE**: `python -c "from jinja2 import Template; Template(open('templates/experiment_templates/research_plan.md.j2').read())"`

### CREATE src/agentic_research/core/templates.py

- **IMPLEMENT**: Template management and rendering system
- **PATTERN**: Class-based template manager with Jinja2 environment
- **IMPORTS**: jinja2, pathlib, typing
- **GOTCHA**: Handle template file not found errors gracefully
- **VALIDATE**: `python -c "from src.agentic_research.core.templates import TemplateManager; tm = TemplateManager()"`

### CREATE src/agentic_research/core/validator.py

- **IMPLEMENT**: Plan validation logic for research methodology compliance
- **PATTERN**: Validator class with rule-based validation methods
- **IMPORTS**: typing, re, dataclasses
- **GOTCHA**: Define clear validation criteria based on research best practices
- **VALIDATE**: `python -c "from src.agentic_research.core.validator import PlanValidator; pv = PlanValidator()"`

### CREATE src/agentic_research/core/planner.py

- **IMPLEMENT**: Main experiment planning logic with AI integration
- **PATTERN**: ExperimentPlanner class with async AI client integration
- **IMPORTS**: openai, anthropic, typing, dataclasses, asyncio
- **GOTCHA**: Handle AI API rate limits and failures with exponential backoff
- **VALIDATE**: `python -c "from src.agentic_research.core.planner import ExperimentPlanner; ep = ExperimentPlanner()"`

### CREATE src/agentic_research/cli/__init__.py

- **IMPLEMENT**: CLI package initialization
- **PATTERN**: Empty init file for package recognition
- **IMPORTS**: None
- **GOTCHA**: None
- **VALIDATE**: `python -c "import src.agentic_research.cli"`

### CREATE src/agentic_research/cli/commands/__init__.py

- **IMPLEMENT**: Commands package initialization
- **PATTERN**: Empty init file for package recognition
- **IMPORTS**: None
- **GOTCHA**: None
- **VALIDATE**: `python -c "import src.agentic_research.cli.commands"`

### CREATE src/agentic_research/cli/commands/plan.py

- **IMPLEMENT**: Plan command implementation with Click decorators
- **PATTERN**: Click command with options for problem statement and dataset description
- **IMPORTS**: click, pathlib, asyncio, src.agentic_research.core.planner
- **GOTCHA**: Handle async operations in Click command context properly
- **VALIDATE**: `python -c "from src.agentic_research.cli.commands.plan import plan"`

### CREATE src/agentic_research/cli/main.py

- **IMPLEMENT**: Main CLI entry point with Click group and command registration
- **PATTERN**: Click group with subcommand registration following Click best practices
- **IMPORTS**: click, src.agentic_research.cli.commands.plan
- **GOTCHA**: Ensure proper command discovery and help text generation
- **VALIDATE**: `python -m src.agentic_research.cli.main --help`

### CREATE tests/unit/test_planner.py

- **IMPLEMENT**: Unit tests for ExperimentPlanner class
- **PATTERN**: Pytest test class with fixtures and mock AI responses
- **IMPORTS**: pytest, unittest.mock, src.agentic_research.core.planner
- **GOTCHA**: Mock AI API calls to avoid external dependencies in tests
- **VALIDATE**: `python -m pytest tests/unit/test_planner.py -v`

### CREATE tests/unit/test_cli.py

- **IMPLEMENT**: Unit tests for CLI commands
- **PATTERN**: Pytest with Click testing utilities
- **IMPORTS**: pytest, click.testing, src.agentic_research.cli.main
- **GOTCHA**: Use Click's CliRunner for proper CLI testing
- **VALIDATE**: `python -m pytest tests/unit/test_cli.py -v`

### CREATE tests/integration/test_plan_generation.py

- **IMPLEMENT**: Integration tests for end-to-end plan generation
- **PATTERN**: Pytest integration tests with real template rendering
- **IMPORTS**: pytest, tempfile, src.agentic_research.core.planner
- **GOTCHA**: Use temporary directories for file output testing
- **VALIDATE**: `python -m pytest tests/integration/test_plan_generation.py -v`

### UPDATE pyproject.toml

- **IMPLEMENT**: Add entry point for CLI command
- **PATTERN**: Poetry-style entry points configuration
- **IMPORTS**: None (configuration file)
- **GOTCHA**: Ensure entry point name matches expected CLI command
- **VALIDATE**: `pip install -e . && agentic-research --help`

---

## TESTING STRATEGY

### Unit Tests

Design unit tests with pytest fixtures and mock objects for external dependencies. Focus on testing individual components in isolation:

- **ExperimentPlanner**: Test hypothesis generation, baseline selection, and metrics recommendation logic
- **TemplateManager**: Test template loading, rendering, and error handling
- **PlanValidator**: Test validation rules and error reporting
- **CLI Commands**: Test argument parsing, validation, and error handling

### Integration Tests

Test complete workflows from CLI input to plan output:

- **End-to-end plan generation**: Test full workflow with sample inputs
- **Template rendering**: Test integration between planner output and template system
- **Configuration loading**: Test configuration file parsing and environment variable handling
- **Error scenarios**: Test graceful handling of API failures and invalid inputs

### Edge Cases

- **Invalid research problems**: Malformed or empty problem statements
- **API failures**: Network errors, rate limiting, invalid API keys
- **Template errors**: Missing templates, rendering failures
- **File system errors**: Permission issues, disk space, invalid paths
- **Large inputs**: Very long problem statements or dataset descriptions

---

## VALIDATION COMMANDS

Execute every command to ensure zero regressions and 100% feature correctness.

### Level 1: Syntax & Style

```bash
# Code formatting
black src/ tests/ --check --diff
isort src/ tests/ --check-only --diff

# Linting
flake8 src/ tests/
pylint src/agentic_research/

# Type checking
mypy src/agentic_research/
```

### Level 2: Unit Tests

```bash
# Run all unit tests with coverage
python -m pytest tests/unit/ -v --cov=src/agentic_research --cov-report=term-missing

# Test specific components
python -m pytest tests/unit/test_planner.py -v
python -m pytest tests/unit/test_cli.py -v
```

### Level 3: Integration Tests

```bash
# Run integration tests
python -m pytest tests/integration/ -v

# Test CLI installation and basic functionality
pip install -e .
agentic-research --help
agentic-research plan --help
```

### Level 4: Manual Validation

```bash
# Test basic plan generation (requires API keys)
export OPENAI_API_KEY="your-key-here"
agentic-research plan --problem "Improve image classification accuracy on CIFAR-10" --dataset "CIFAR-10 dataset with 60,000 32x32 color images in 10 classes"

# Test output file generation
agentic-research plan --problem "Sentiment analysis for movie reviews" --dataset "IMDB movie review dataset" --output experiment_plan.md
cat experiment_plan.md
```

### Level 5: Additional Validation (Optional)

```bash
# Package building
python -m build
twine check dist/*

# Documentation generation (if implemented)
sphinx-build -b html docs/ docs/_build/html/
```

---

## ACCEPTANCE CRITERIA

- [ ] CLI accepts research problem statement and dataset description as input
- [ ] Generated experiment plans include clear, testable research hypotheses
- [ ] Baseline model recommendations are provided with justification
- [ ] Evaluation metrics are suggested with domain-appropriate reasoning
- [ ] Step-by-step experiment procedures are included in output
- [ ] Reproducibility checks and requirements are specified
- [ ] Plans are output as structured markdown documents
- [ ] All validation commands pass with zero errors
- [ ] Unit test coverage meets 80%+ requirement
- [ ] Integration tests verify end-to-end workflow functionality
- [ ] Code follows PEP 8 and project conventions
- [ ] CLI provides helpful error messages for invalid inputs
- [ ] AI API failures are handled gracefully with informative messages
- [ ] Configuration supports multiple AI providers (OpenAI, Anthropic)
- [ ] Template system allows for customizable plan formats

---

## COMPLETION CHECKLIST

- [ ] All tasks completed in dependency order
- [ ] Each task validation passed immediately after implementation
- [ ] All validation commands executed successfully
- [ ] Full test suite passes (unit + integration)
- [ ] No linting, formatting, or type checking errors
- [ ] Manual testing confirms CLI functionality works as expected
- [ ] Acceptance criteria all verified and met
- [ ] Code reviewed for quality, maintainability, and adherence to patterns
- [ ] Documentation strings added to all public functions and classes
- [ ] Error handling implemented for all failure scenarios

---

## NOTES

**Design Decisions:**
- Chose Click over Typer for CLI framework due to mature ecosystem and extensive documentation
- Implemented async AI client integration to support future concurrent processing
- Used Jinja2 templates for flexible plan formatting and future customization
- Pydantic for configuration validation ensures type safety and clear error messages

**Trade-offs:**
- AI dependency requires API keys but provides intelligent analysis capabilities
- Template-based output allows customization but adds complexity
- Async implementation adds complexity but enables future performance improvements

**Future Considerations:**
- Support for multiple AI providers with fallback mechanisms
- Custom template creation and management features
- Integration with experiment tracking tools (MLflow, W&B)
- Batch processing of multiple research problems
- Web interface for non-CLI users
