# Software Engineering Lab Repository (UE24CS341A)

**Ashrit Nair · PES2UG24AM032 · Section 5A** · PES University, Dept. of CSE

This repository holds my lab work and the Mini Project, following the course lesson plan.

## Labs

| Lesson plan item | Level | Folder | Scenario / assigned repo | Deliverables |
|---|---|---|---|---|
| Lab 1 – Requirements Engineering & UML Use-Case Modelling | L1 | [Lab 1](Lab%201/) | Problem #29 – Municipal Infrastructure Damage Reporting App | Requirements table (5 FR, 2 NFR), use-case diagram, use-case flow |
| Lab 2 – Jira: Agile Backlog Creation & Sprint Simulation | L2 | [Lab 2](Lab%202/) | Problem #29 | 4 epics, 10 stories (45 SP), 2 sprints, burndown charts, reflection PDF |
| Lab 3 – Architectural Pattern Selection & Component Diagram | L1 | [Lab 3](Lab%203/) | Problem #29 | UML component diagram (7 components, 7 interfaces), 1-page justification |
| Lab 4 – Advanced Vibe Coding & AI-Assisted Development | L1 | [Lab 4](Lab%204/) | Dig Dug Repair Lab (Pygame) | Repaired game, before/after videos, AI chat history |
| Lab 5 – Static Code Analysis | L2 | [Lab 5](Lab%205/) | `L5_29_digital_wallet` | Pylint/Flake8/Bandit reports before and after, issues table, reflection |
| Lab 6 – Code and Branch Coverage Analysis | L2 | [Lab 6](Lab%206/) | `L6_L7_29_thermostat_control` | Code-coverage and branch-coverage test files (100% / 100%), terminal screenshots |
| Lab 7 – Fuzzing for Input Validation Bugs | L2 | [Lab 7](Lab%207/) | `L6_L7_29_thermostat_control` | Hypothesis fuzz tests (8 fail → 11 pass), fixed application, screenshots |

## Mini Project (Level 3) – Dehallucination Module (DAM)

Team 39 · Team repository: [SE-MiniProject-Team-39/dehallucination-module](https://github.com/SE-MiniProject-Team-39/dehallucination-module). [MiniProject](MiniProject/) holds a snapshot of the merged code.

| Lesson plan deliverable | Where |
|---|---|
| D1 – Project SRS | [Dehallucination_Module_SRS_Phase1.pdf](MiniProject/Dehallucination_Module_SRS_Phase1.pdf) |
| D2 – Test plan; complete backlog | [TEST_PLAN.md](MiniProject/docs/TEST_PLAN.md), [backlog.csv](MiniProject/docs/backlog.csv) (stories also tracked as GitHub issues in the team repo) |
| D3/D4 – Architecture / design | [ARCHITECTURE.md](MiniProject/docs/ARCHITECTURE.md), [TRACEABILITY.md](MiniProject/docs/TRACEABILITY.md) |
| Sprint 1 & 2 – implementation, unit/integration/system tests, CI/CD | [backend](MiniProject/backend/), [frontend](MiniProject/frontend/), [testing](MiniProject/testing/) (32 documented cases across 4 levels), CI: [.github/workflows/miniproject.yml](.github/workflows/miniproject.yml) |
| Final – test reports incl. code & branch coverage | [TEST_RESULTS.md](MiniProject/docs/TEST_RESULTS.md) (203 tests passing), [COVERAGE.md](MiniProject/docs/COVERAGE.md) (98.3% combined, 94.5% branch) |

My contributions are the backend core and claim extraction (PRs #4–#8), the coverage report and CI coverage gate, and the formal test plan. See [ashrit-core-extraction.md](MiniProject/docs/ashrit-core-extraction.md).
