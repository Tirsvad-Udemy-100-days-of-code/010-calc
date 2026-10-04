# MIL-001 Project scaffold

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [PP-001], [SA-001], [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8ccefff] |

---

## Purpose

Decide whether the repository is ready for code: layout, tooling and configuration exist and a fresh clone can create a local virtual environment.

## Deliverable

`pyproject.toml`, Python `.gitignore`, `src/calc/` and `tests/` skeletons, `Doxyfile`, repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` requires Python 3.13 or newer and has no runtime dependencies | Met | Not met |
| 2 | `.gitignore` covers `.venv`, `.env` and `docs/doxygen/` | Met | Not met |
| 3 | Folders `src/`, `tests/` and `docs/` exist | Met | Not met |
| 4 | Repository description and topics are set on the git host | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

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

2026-10-05

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Project configuration: name, version, Python 3.13+ requirement, empty runtime dependencies, `dev` extra with pytest, console script `calc`, pytest settings. | No |  |
| 2 | Add Python .gitignore and folder layout | Python `.gitignore` that also ignores `.env`, `.venv` and `docs/doxygen/`; create `src/calc/` and `tests/`. | No |  |
| 3 | Add Doxyfile | Doxygen configuration reading `src/`, writing to `docs/doxygen/`, so Doxygen-style comments can be built into API docs. | No |  |
| 4 | Set repository description and topics | Set the description and topics on the git host repository through its API, with the token from `.env`, which is personal tooling and never part of the project. | No |  |

---

[PP-001]: ../project-plan.md
[SA-001]: ../stakeholder-analysis.md
[BC-001]: ../business-case.md
[8ccefff]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/010-calc/commit/8ccefffef7ec1f9ecbf548085a5c92fae75e1341
