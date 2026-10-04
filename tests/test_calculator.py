"""!
@file test_calculator.py
@brief Tests for the interactive calculator loop.
"""

import pytest

from calc.calculator import calculator, format_number, main


def feed(monkeypatch: pytest.MonkeyPatch, answers: list[str]) -> None:
    """!
    @brief Make input() return the given answers in order.
    @param monkeypatch The pytest monkeypatch fixture.
    @param answers The lines the "user" types.
    """
    lines = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(lines))


def test_format_number_drops_trailing_zero() -> None:
    assert format_number(5.0) == "5"
    assert format_number(2.5) == "2.5"


def test_calculator_adds_then_quits(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    feed(monkeypatch, ["2", "+", "3", "q"])
    calculator()
    assert "2 + 3 = 5" in capsys.readouterr().out


def test_calculator_continues_with_previous_result(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    feed(monkeypatch, ["2", "+", "3", "y", "*", "4", "q"])
    calculator()
    assert "5 * 4 = 20" in capsys.readouterr().out


def test_calculator_starts_new_calculation(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    feed(monkeypatch, ["2", "+", "3", "n", "10", "/", "4", "q"])
    calculator()
    assert "10 / 4 = 2.5" in capsys.readouterr().out


def test_calculator_reprompts_on_invalid_input(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    feed(monkeypatch, ["abc", "1", "^", "+", "x", "1", "?", "q"])
    calculator()
    out = capsys.readouterr().out
    assert "not a number" in out
    assert "not a valid operation" in out
    assert "Please answer" in out
    assert "1 + 1 = 2" in out


def test_calculator_restarts_after_division_by_zero(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    feed(monkeypatch, ["1", "/", "0", "6", "-", "1", "q"])
    calculator()
    out = capsys.readouterr().out
    assert "cannot divide by zero" in out
    assert "6 - 1 = 5" in out


def test_main_shows_ascii_art(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    feed(monkeypatch, ["1", "+", "1", "q"])
    main()
    out = capsys.readouterr().out
    assert "|_____________________|" in out
    assert "Goodbye!" in out
