# Asteroids Game

A simple implementation of the classic Asteroids game using Pygame.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd asteroids
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install the package in development mode with testing dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Running the Game

To start the game, run:

```bash
python -m asteroids
```

## Controls

- `ESC` - Quit the game
- `X` (window close button) - Quit the game

## Running Tests

To run the test suite:

```bash
pytest
```

## Project Structure

```
asteroids/
├── src/
│   └── asteroids/
│       ├── __init__.py
│       ├── __main__.py
│       └── game.py
├── tests/
│   ├── __init__.py
│   └── test_game.py
├── pyproject.toml
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
