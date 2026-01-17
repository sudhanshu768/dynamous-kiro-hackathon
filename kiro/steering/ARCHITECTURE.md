# Architecture & Steering Rules

## Project
Agentic Research Engineer CLI

## Goal
Convert high-level research problems into structured machine learning
experiment plans using deterministic logic with optional AI assistance.

## Design Principles
- Deterministic fallback must always work
- AI assistance must never crash the CLI
- Human-in-the-loop AI usage is intentional
- Planning ≠ training or execution
- No dataset is required at planning stage

## AI Usage Policy
- Kiro is used to assist hypothesis generation
- AI outputs are reviewed and curated by the user
- The system remains usable without AI

## Why This Design
This ensures robustness, reproducibility, and explainability while still
demonstrating effective use of AI tools during research ideation.

