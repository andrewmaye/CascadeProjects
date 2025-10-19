---
trigger: always_on
---

# 🧭 Python Development Rules — Windsurf Cascade Configuration

## 🎯 Overview
These rules define the development, quality, and design standards for generating and maintaining Python software in this workspace.  
They apply to **command-line tools**, **simple utilities**, and **pygame-based 2D games**.

All generated code should:
- Be **maintainable**, **testable**, and **readable**.
- Follow **Python community standards** (PEP8, PEP257, PEP484, PEP561, etc.).
- Adhere to **software engineering best practices**, including **SOLID** principles.

---

## 🧱 Project Structure

Each project should use a **modern, modular layout**:

```
project_name/
│
├── pyproject.toml          # Build system + tool config (use Poetry or Hatch)
├── README.md               # Overview + usage examples
├── requirements.txt        # Optional fallback for pip
├── .gitignore
│
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py         # CLI entrypoint or pygame app
│       ├── core/           # Core logic / business rules
│       ├── cli/            # CLI argument parsing (if applicable)
│       ├── game/           # Pygame-specific modules
│       └── utils/          # Helpers / shared functions
│
└── tests/
    ├── __init__.py
    └── test_*.py           # Unit tests (pytest)
```

---

## 🧩 Coding Standards

### General
- Follow **PEP8** style conventions.
- Use **snake_case** for functions and variables, **PascalCase** for classes, **SCREAMING_SNAKE_CASE** for constants.
- Every module and class should have a clear, single responsibility.
- Avoid deep nesting; prefer early returns and composable functions.

### Type Annotations
- Use **full type hints** everywhere (PEP484).
- Run **mypy** or **pyright** for static type checking.
- Example:

```python
def load_config(path: Path) -> dict[str, Any]:
    ...
```

### Docstrings
- Use **PEP257-compliant** docstrings with **Google-style** formatting.
- Every public function, class, and module must have docstrings.

Example:
```python
def calculate_score(points: list[int]) -> int:
    """Calculate the total score from a list of points.

    Args:
        points: List of individual scores.

    Returns:
        The total accumulated score.
    """
```

---

## 🧰 Tooling and Quality Gates

### Core Tools
| Purpose | Tool | Notes |
|----------|------|-------|
| Dependency & build | `poetry` or `hatch` | Use `pyproject.toml` for config |
| Linting | `ruff` | Fast + modern; replaces flake8/isort |
| Formatting | `black` | Opinionated formatter |
| Type Checking | `mypy` or `pyright` | Enforce strict typing |
| Testing | `pytest` | Use fixtures + mocks |
| Coverage | `pytest-cov` | Aim ≥ 90% coverage |
| Static Analysis | `bandit` | Security scanner |

### Example `pyproject.toml` Snippet

```toml
[tool.black]
line-length = 88

[tool.ruff]
select = ["E", "F", "I", "B"]
line-length = 88
ignore = ["E501"]

[tool.mypy]
strict = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov=src --cov-report=term-missing"
```

---

## 🧠 Software Engineering Principles

Follow **SOLID** and **clean architecture** principles.

| Principle | Summary | Application |
|------------|----------|--------------|
| **S**ingle Responsibility | One reason to change | Separate logic into clear modules |
| **O**pen/Closed | Open for extension, closed for modification | Use abstraction + composition |
| **L**iskov Substitution | Subtypes must behave like base types | Respect inheritance contracts |
| **I**nterface Segregation | Don’t force unused methods | Use small, focused classes/interfaces |
| **D**ependency Inversion | Depend on abstractions, not concretes | Inject dependencies |

For games:
- Separate **game logic** (entities, physics, scoring) from **rendering/input**.
- Use **Entity-Component-System (ECS)** or **state-driven architecture** where appropriate.

---

## ⚙️ Command-Line Programs

- Use **`argparse`** or **`typer`** (preferred) for CLI interfaces.
- Always include `--help` and subcommands if applicable.
- Example:

```python
import typer

app = typer.Typer()

@app.command()
def greet(name: str):
    """Greet a user by name."""
    typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()
```

---

## 🕹️ Pygame Projects

- Keep the **game loop** lean — delegate logic to subsystems.
- Use **composition over inheritance** for entities.
- Separate:
  - **`game/engine.py`** — loop + timing + events
  - **`game/entities.py`** — sprites, logic
  - **`game/scenes/`** — levels, menus, UI
- Store assets under `assets/`.

Example game loop snippet:

```python
while running:
    dt = clock.tick(60) / 1000.0
    handle_events()
    update(dt)
    render(screen)
```

---

## 🧪 Testing Guidelines

- Use `pytest` with `unittest.mock` or `pytest-mock`.
- Unit tests should **not** depend on I/O, APIs, or rendering.
- For pygame, abstract the display to allow headless testing.

Example test:

```python
def test_calculate_score():
    from src.project_name.core.scoring import calculate_score
    assert calculate_score([1, 2, 3]) == 6
```

---

## 🧩 Git & CI

- Use conventional commits (`feat:`, `fix:`, `refactor:`, `test:`).
- Include `.pre-commit` hooks for lint/format.
- Run `pytest`, `ruff`, `black --check`, and `mypy` in CI.

---

## 🧠 AI Agent Guidelines

When generating or refactoring code:
1. Use **explicit typing** and **docstrings**.
2. Organize modules logically under `src/`.
3. Add **tests** for every new feature or bug fix.
4. Apply **lint**, **format**, and **type check** before finalizing.
5. Avoid hidden global state or side effects.
6. Follow SOLID principles.
7. Prefer clarity and maintainability over brevity.

---

## ✅ Summary Checklist

| Category | Tool/Rule | Status |
|-----------|------------|--------|
| Code Style | PEP8 / Black | ✅ |
| Linting | Ruff | ✅ |
| Typing | Mypy / Pyright | ✅ |
| Testing | Pytest | ✅ |
| Architecture | SOLID, modular design | ✅ |
| Game Dev | Pygame best practices | ✅ |

---

_This rules file ensures consistency, maintainability, and professional-grade quality across all Python projects created with agentic AI assistance._
