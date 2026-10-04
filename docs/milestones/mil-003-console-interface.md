# MIL-003 Console interface

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [PP-001], [SA-001], [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8ccefff] |

---

## Purpose

Decide whether the interactive calculator behaves as the lecture describes, including continuing with the result and restarting by recursion.

## Deliverable

`src/calc/calculator.py` and `src/calc/__main__.py` with the ASCII title and calculator, input handling and the recursive restart, plus `tests/test_calculator.py`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The program asks for a number, an operation and a second number | Met | Not met |
| 2 | Answer `y` continues with the previous result, `n` starts a new calculation by calling `calculator()` again, `q` quits | Met | Not met |
| 3 | Invalid numbers, operations and answers are re-prompted; division by zero restarts the calculator | Met | Not met |
| 4 | ASCII title and ASCII calculator are shown at start | Met | Not met |
| 5 | `python -m calc` runs and the tests pass | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Uses the operations dictionary and constants |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-07

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the calculator loop with recursive restart | `calculator()` reads the numbers and operation, looks the function up in `OPERATIONS`, and lets the user continue with the result or call `calculator()` again for a new calculation. | No |  |
| 2 | Add ASCII title and ASCII calculator | Show the ASCII title and an ASCII calculator when the program starts, taken from `constants.py`. | No |  |
| 3 | Handle invalid input and division by zero | Re-prompt on non-numeric input, unknown operations and unknown answers; print a message and restart on division by zero. | No |  |
| 4 | Add interface tests | pytest tests that feed `input()` through monkeypatch and check the printed results, the continue and new paths, re-prompts and the ASCII art. | No |  |

---

[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
[BC-001]: ../business-case.md
[8ccefff]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/010-calc/commit/8ccefffef7ec1f9ecbf548085a5c92fae75e1341
