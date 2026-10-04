# 🧮 Calculator

A beginner-friendly Python console program that adds, subtracts, multiplies and divides numbers, and lets you keep calculating with the previous result.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)

## 🧭 Overview

Final project of Day 10 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*. The program shows an ASCII calculator with the title beside it, then asks for a number, an operation (`+`, `-`, `*`, `/`) and a second number.

The operations are functions stored in a dictionary (`OPERATIONS` in `src/calc/operations.py`) and called through it. After each result you can continue with it (`y`), start a new calculation (`n`, which calls `calculator()` again through recursion) or quit (`q`). Invalid input is asked for again, and dividing by zero starts over with a message.

## 📋 Requirements

- Python 3.13 or newer
- No runtime dependencies
- `pytest` for the tests (installed with the `dev` extra)
- Optional: [Doxygen](https://www.doxygen.nl/) to build the API documentation

## 🛠️ Setup

Create a local virtual environment in the project folder:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Upgrade pip and install the project with the test tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. The `.env` file in the repository is for personal tooling only; the project never reads or imports it.

## ▶️ Run

With the environment active:

```bash
python -m calc
```

or, since the install adds a console script, simply:

```bash
calc
```

## 🧪 Tests

```bash
python -m pytest
```

Build the API documentation from the Doxygen comments (written to `docs/doxygen/`):

```bash
doxygen Doxyfile
```

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE](LICENSE).

## 🔗 Links

- [Repository](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code)
- [Documentation](docs/doxygen/html/index.html) (generated with `doxygen Doxyfile`)
- [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/010-calc/issues)
