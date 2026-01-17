# DEVLOG — Agentic Research Engineer CLI

## Day 1 – Project Setup
- Cloned Dynamous × Kiro hackathon template
- Defined project goal: convert research ideas into structured experiment plans
- Set up Python CLI using Click
- Established deterministic-first design philosophy

## Day 2 – Core CLI & Planning Logic
- Implemented `agentic-research plan` command
- Built deterministic experiment planner
- Added input validation with warnings and errors
- Ensured tool works without datasets or AI dependency

## Day 3 – Markdown Rendering & Output
- Designed Jinja2 template for experiment plans
- Implemented markdown rendering pipeline
- Fixed rendering bug where output file was empty
- Verified correct file generation

## Day 4 – AI-Assisted Ideation with Kiro
- Used Kiro CLI to brainstorm research hypotheses
- Adopted human-in-the-loop workflow:
  - AI assists ideation
  - Deterministic logic ensures reproducibility
- Decided not to auto-execute AI calls to preserve reliability

## Key Design Decisions
- Deterministic fallback is always available
- AI is optional and assistive, never required
- Tool focuses on planning, not training or execution

## Challenges Faced
- CLI argument validation edge cases
- Markdown rendering bug (empty output)
- Integrating AI ideas without breaking determinism

## How Kiro Was Used
- Hypothesis generation
- Experiment design refinement
- Debugging assistance
- Documentation improvement

