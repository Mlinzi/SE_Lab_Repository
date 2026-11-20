# Software Engineering Lab Repository (UE24CS341A)

**Ashrit Nair · PES2UG24AM032 · Section 5A** · PES University, Dept. of CSE

This repository holds my lab work and the Mini Project, following the course lesson plan.

## Labs

| Lesson plan item | Level | Folder | Scenario / assigned repo | Deliverables |
|---|---|---|---|---|
| Lab 1 – Requirements Engineering & UML Use-Case Modelling | L1 | [Lab 1](Lab%201/) | Problem #29 – Municipal Infrastructure Damage Reporting App | Requirements table (5 FR, 2 NFR), use-case diagram, use-case flow |
| Lab 2 – Jira: Agile Backlog Creation & Sprint Simulation | L2 | [Lab 2](Lab%202/) | Problem #29 | 4 epics, 10 stories (45 SP), 2 sprints, burndown charts, reflection PDF |
| Lab 3 – Architectural Pattern Selection & Component Diagram | L1 | [Lab 3](Lab%203/) | Problem #29 | UML component diagram (7 components, 7 interfaces), 1-page justification |
| Lab 4 – Advanced Vibe Coding & AI-Assisted Development | L1 | [Lab 4](Lab%204/) | Dig Dug Repair Lab (Pygame) | Repaired game (one commit per task in the [fork](https://github.com/Mlinzi/32_digDug/commits)), before/after videos, AI chat history |
| Lab 5 – Static Code Analysis | L2 | [Lab 5](Lab%205/) | `L5_29_digital_wallet` | Pylint/Flake8/Bandit reports before and after (Pylint 5.69 → 10.00), one fix commit per tool, issues table, reflection |
| Lab 6 – Code and Branch Coverage Analysis | L2 | [Lab 6](Lab%206/) | `L6_L7_29_thermostat_control` | Code-coverage and branch-coverage test files (100% / 100%), terminal screenshots |
| Lab 7 – Fuzzing for Input Validation Bugs | L2 | [Lab 7](Lab%207/) | `L6_L7_29_thermostat_control` | Hypothesis fuzz tests (8 fail → 11 pass), fixed application, screenshots |

## Mini Project (Level 3) – Dehallucination Module (DAM)

Team 39 · Team repository: [SE-MiniProject-Team-39/dehallucination-module](https://github.com/SE-MiniProject-Team-39/dehallucination-module). All Mini Project code and documents live in the team repository; Its [README](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/README.md) and [DELIVERY.md](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/DELIVERY.md) list where each deliverable is.

| Lesson plan deliverable | Where |
|---|---|
| D1 – Project SRS | [Dehallucination_Module_SRS_Phase1.pdf](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/Dehallucination_Module_SRS_Phase1.pdf) |
| D2 – Test plan; complete backlog | [TEST_PLAN.md](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/TEST_PLAN.md), [backlog.csv](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/backlog.csv) (14 stories, 65 points, two sprints, tracked as GitHub issues on the team's "DAM 1.0 Backlog" project) |
| D3/D4 – Software Architecture Document / Software Design Document | [SAD](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/DAM_Software_Architecture_Document_SAD.docx), [SDD](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/DAM_Software_Design_Document.docx), [ARCHITECTURE.md](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/ARCHITECTURE.md) with [system](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/architecture.png) and [pipeline](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/pipeline.png) diagrams, [TRACEABILITY.md](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/TRACEABILITY.md) |
| Sprint 1 & 2 – implementation, unit/integration/system tests, CI/CD | [backend](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/backend/), [frontend](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/frontend/), [testing](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/testing/) (32 documented cases across 4 levels), CI: [GitHub Actions](https://github.com/SE-MiniProject-Team-39/dehallucination-module/actions) |
| Sprint demo videos (working product) | [Sprint 1 – 1 min](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/sprint-1.mp4), [Sprint 2 – 2 min](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/sprint-2.mp4) |
| Final – test reports incl. code & branch coverage | [TEST_RESULTS.md](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/TEST_RESULTS.md) (315 tests passing; browser end-to-end, Docker/PostgreSQL, live-source and LLM evidence-judge checks), [COVERAGE.md](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/COVERAGE.md) (96.5% combined, 92.4% branch) |

My contributions are the backend core and claim extraction (PRs #4–#8), the coverage report and CI coverage gate, and the formal test plan. See [ashrit-core-extraction.md](https://github.com/SE-MiniProject-Team-39/dehallucination-module/blob/main/docs/ashrit-core-extraction.md).
