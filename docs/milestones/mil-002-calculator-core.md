# MIL-002 Calculator core

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [PP-001], [SA-001], [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8ccefff] |

---

## Purpose

Decide whether the arithmetic core is correct and tested before the console interface is built on it.

## Deliverable

`src/calc/constants.py` and `src/calc/operations.py` with add, subtract, multiply, divide and the `OPERATIONS` dictionary, plus `tests/test_operations.py`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The four operations return correct results in the tests | Met | Not met |
| 2 | Division by zero raises `ZeroDivisionError` | Met | Not met |
| 3 | `OPERATIONS` maps `+ - * /` to the stored (not called) functions | Met | Not met |
| 4 | All constants live in `constants.py` | Met | Not met |
| 5 | Every function has a Doxygen comment | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the package layout and configuration |

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

2026-10-06

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add constants module | `constants.py` holding operation symbols, answers, prompts, messages and the ASCII art, so no literals are scattered through the code. | No |  |
| 2 | Implement the four operations and the OPERATIONS dictionary | Functions `add`, `subtract`, `multiply`, `divide` and a dictionary mapping each symbol to its function, stored without calling them, as taught in the lecture. | No |  |
| 3 | Add operation tests | pytest tests for each operation, division by zero and the dictionary contents. | No |  |

---

[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
[BC-001]: ../business-case.md
[8ccefff]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/010-calc/commit/8ccefffef7ec1f9ecbf548085a5c92fae75e1341
