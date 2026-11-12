# Lab 2 – Agile Backlog Creation & Sprint Simulation in Jira

**Problem Statement #29 – Municipal Infrastructure Damage Reporting App.** The backlog is derived from the Lab 1 requirements FR-001 to FR-005, NFR-001 and NFR-002.

## Backlog

| Epic | Story | Req | Priority | Points | Sprint |
|---|---|---|---|---:|---|
| EPIC1 Damage Reporting | Auto-detect report location | FR-001 | High | 5 | 1 |
| | Choose damage type and attach photo | FR-002 | High | 3 | 1 |
| | Submit report offline | NFR-001 | High | 8 | 2 |
| EPIC2 Automated Screening | Flag duplicate reports | FR-003 | High | 8 | 1 |
| | Reject incomplete or out-of-city reports | FR-003 | High | 3 | 1 |
| EPIC3 Routing and Resolution | Route valid report to department | FR-004 | High | 5 | 1 |
| | Assign engineer and update status | FR-004 | High | 3 | 2 |
| | Audit log of status changes | NFR-002 | High | 5 | 2 |
| EPIC4 Status Tracking and Notifications | Track report status | FR-005 | Medium | 2 | 2 |
| | Notify on status change | FR-005 | Medium | 3 | 2 |

**Sprint 1 (1 week): 24 points.** Goal: a citizen can submit a located, photographed report that is screened and reaches the right department.
**Sprint 2 (1 week): 21 points.** Goal: offline submission, officer workflow with audit trail, and citizen status tracking and notifications.

Story points use the Fibonacci scale. Offline sync (8) and duplicate detection (8) carry the most uncertainty: sync conflicts and deciding when two reports describe the same damage.

`Jira_Backlog_Import.csv` holds the full user-story text (*As a … I want … so that …*) for each item. Each story can be typed into Jira as written, or the file can be loaded through **Settings → System → External system import → CSV**.

## Deliverables
| File | Content |
|---|---|
| `Lab2_Submission.pdf` | Backlog summary, answers to the 4 reflection questions, and all screenshots |
| `screenshots/1_backlog_epics_story_points.png` | Backlog with the Epic panel, 10 stories, priorities and story points (45) |
| `screenshots/2_sprint1_active_board.png` | Sprint 1 active sprint board |
| `screenshots/3_sprint1_burndown.png` | Sprint 1 completed: burndown (24/24 points) |
| `screenshots/4_sprint2_burndown.png` | Sprint 2 completed: burndown (21/21 points), all epics 100% |
