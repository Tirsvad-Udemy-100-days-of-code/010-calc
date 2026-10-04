# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [8ccefff] |

---

## Purpose

Name the one stakeholder of this very small project, so that owners and reviewers in the other documents can cite a stakeholder ID. The project is a single-person course assignment with a short Business Case ([BC-001]).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Product Owner | Tirsvad | HIGH | HIGH | Manage Closely | A working, tested, documented console calculator that matches the lecture |

## Power/Interest Classification Rationale

S01 decides scope, does the work and accepts every milestone, so S01 is managed closely.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Operations stored in a dictionary, continue with result, restart by recursion | Functionality |
| S01 | Simple setup with a local venv and no runtime dependencies | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat | Per milestone | Working-tree changes and summary | MIL-001 to MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| None, there is one stakeholder | S01 | Not applicable |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Finish the day 10 assignment | Objectives 1 to 4 in [BC-001] |

## Sign-Off

Accepted by S01.

---

[BC-001]: ./business-case.md
[8ccefff]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/010-calc/commit/8ccefffef7ec1f9ecbf548085a5c92fae75e1341
