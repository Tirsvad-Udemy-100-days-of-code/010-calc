# MIL-004 Documentation and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [PP-001], [SA-001], [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8ccefff] |

---

## Purpose

Decide whether the project can be handed over: a new user can set it up, run it and test it from the README alone.

## Deliverable

`README.md` following the project template, Doxygen output building without warnings, AGPL licence referenced.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README has Overview, Requirements, Setup, Run, Tests, License and Links | Met | Not met |
| 2 | README explains creating `.venv` and `python -m pip install --upgrade pip` | Met | Not met |
| 3 | `doxygen Doxyfile` builds with no warnings | Met | Not met |
| 4 | Following the README on a clean clone, the program runs and the tests pass | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Documents the finished program |

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

2026-10-08

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write README.md | README from the project template with calculator-specific text: venv setup, pip upgrade, run, tests, AGPL license and links. | No |  |
| 2 | Verify Doxygen build | Run `doxygen Doxyfile` and fix any warnings so every module and function is documented. | No |  |
| 3 | Verify setup from a clean clone | Follow the README in a fresh `.venv` to confirm install, run and test commands work as written. | No |  |

---

[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
[BC-001]: ../business-case.md
[8ccefff]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/010-calc/commit/8ccefffef7ec1f9ecbf548085a5c92fae75e1341
