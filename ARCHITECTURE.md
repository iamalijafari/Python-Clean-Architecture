# Python Clean Architecture

This repository is a minimal starting point for a Python backend organized around Clean Architecture principles.

## Proposed boundaries

- `api`: HTTP transport and request/response handling.
- `application`: use cases and orchestration.
- `domain`: business rules and domain models.
- `infrastructure`: implementations for persistence and external integrations.

## Dependency rule

Dependencies should point inward: `api` and `infrastructure` may depend on application/domain abstractions, while the domain remains independent of frameworks and infrastructure. Keep this template minimal until the actual product requirements are known.
