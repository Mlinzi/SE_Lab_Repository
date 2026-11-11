# Lab 3 – Component Modelling & Architectural Pattern Selection

**Problem Statement #29 – Municipal Infrastructure Damage Reporting App** (same scenario as Lab 1 and Lab 2)

## Deliverables
| File | Description |
|------|-------------|
| `Component_Diagram.png` | UML component diagram: 7 components and 7 provided/required (ball-and-socket) interfaces, grouped into client tier, application server, and data & external services |
| `Component_Diagram.svg` | Vector source of the same diagram |
| `Architecture_Justification.docx` / `.pdf` | One-page justification: chosen architecture, two reasons, security advantage, performance benefit |

## Architecture: Client-Server (layered municipal server)

| Component | Responsibility | Requirements |
|---|---|---|
| Citizen Mobile App | Capture the geotagged photo and description, queue reports offline | FR-001, FR-002, NFR-001 |
| Officer Dashboard | Review reports, assign an engineer, update status | FR-004 |
| Report Manager | Report lifecycle and routing (core server component) | FR-001, FR-002, FR-004 |
| Screening Service | Check for duplicates, missing photos and out-of-city locations | FR-003 |
| Dispatch & Notification | Department routing queue and citizen push alerts | FR-005 |
| Report & Audit Store | Reports, photos, append-only status audit log | NFR-002 |
| Geolocation / Map API (external) | Convert GPS to an address and ward, look up the city boundary | FR-001, FR-003 |

## Interfaces
| Interface | Provider → Requirer | Technology |
|---|---|---|
| IReportSubmission | Report Manager → Citizen Mobile App | REST/HTTPS + JSON |
| IOfficerWorkflow | Report Manager → Officer Dashboard | REST/HTTPS, role-based |
| IScreening | Screening Service → Report Manager | Internal API call |
| IDispatch | Dispatch & Notification → Report Manager | Message queue |
| IReportRepository | Report & Audit Store → Report Manager | SQL / ORM |
| IGeocoding | Geolocation / Map API → Screening Service | HTTPS map API |
| IStatusNotification | Dispatch & Notification → Citizen Mobile App | Push notification (FCM) |
