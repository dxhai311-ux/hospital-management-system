# Hospital Management System

A production-style Hospital Management System project built from scratch to learn database design and data engineering, following a real-world software development process — from requirement gathering to a working PostgreSQL database with tested constraints, indexes, views, and business-scenario SQL queries.

This project is part of a self-designed Data Engineering learning roadmap, where the Hospital Management System serves as the end-to-end practice vehicle from requirements analysis through eventual ETL / Data Warehouse work.

## Status

🚧 In Progress — currently paused after completing Database Design, Database Implementation, and part of SQL Practice. See [Roadmap Progress](#roadmap-progress) below for exact status.

## Tech Stack

- **Database:** PostgreSQL
- **Client tool:** DBeaver
- **Version control:** Git / GitHub
- **Diagramming:** draw.io (crow's foot notation)
- **Editor:** VS Code

## Project Structure

```
hospital-management-system/
├── diagrams/
│   ├── conceptual_erd.drawio / .png
│   ├── logical_erd.drawio / .png
│   └── physical_erd.drawio / .png
├── docs/
│   ├── requirement.md            # Software Requirement Specification
│   ├── business_analysis.md      # Actors, business process, business rules
│   ├── entities.md               # Entity analysis (why each table exists)
│   ├── attributes.md             # Attribute-level analysis per entity
│   ├── realationships.md         # Relationship analysis (cardinality, participation)
│   ├── erd_design.md             # ERD design principles and entity grouping
│   ├── normalization.md          # 1NF/2NF/3NF analysis for all 11 tables
│   └── physical_design.md        # PostgreSQL data type decisions per column
├── notes/                        # Personal study notes (Vietnamese-friendly), one per topic
├── sql/
│   ├── V001–V011                 # CREATE TABLE migrations (11 tables)
│   ├── V012–V022                 # NOT NULL constraints
│   ├── V023–V029                 # UNIQUE constraints (including composite)
│   ├── V030–V038                 # CHECK constraints
│   ├── V039–V045                 # DEFAULT values
│   ├── V046–V051                 # Indexes
│   ├── V052–V057                 # Views
│   ├── V058–V068                 # Sample data inserts
│   └── queries.sql               # SQL Practice — business-scenario queries (Q1, Q2, ...)
└── README.md
```

## Database Design

The system models a single-hospital, single-branch Hospital Management System covering:

- **Patient Management** — patient records, contact info
- **Doctor Management** — doctors, specialties, department assignment
- **Department & Room Management** — hospital departments and physical rooms
- **Appointment Management** — scheduling between patients, doctors, and rooms
- **Medical Record Management** — diagnosis, symptoms, treatment per appointment
- **Prescription Management** — prescriptions and prescribed medicine items
- **Medicine Management** — medicine catalog and stock
- **Billing** — invoices and payments

**11 entities**, normalized to 3NF, with PostgreSQL-specific physical data types (e.g. `VARCHAR` vs `TEXT` chosen deliberately per column, `DECIMAL` for all monetary values, never `FLOAT`).

See `diagrams/logical_erd.png` and `diagrams/physical_erd.png` for the full entity-relationship diagrams.

## Database Implementation

All schema changes are tracked as sequential, Flyway-style migrations (`V0XX__description.sql`) in `sql/`, following the principle of never modifying a migration once it has been "released" — every later change (adding a constraint, a default value, an index) is a new migration file, never an edit to an old one.

- **Constraints:** `NOT NULL`, `UNIQUE` (including composite keys), `CHECK`, and `DEFAULT` values across all 11 tables — each backed by a documented business reason (e.g. `UNIQUE` on a 1:1 relationship's foreign key, since a foreign key alone does not prevent duplicate rows).
- **Indexes:** added only on columns that are both frequently queried and not already covered by a `UNIQUE`/`PRIMARY KEY` index, based on realistic query patterns (e.g. filtering appointments by doctor or date), not on every column.
- **Views:** 5 views — 4 detail views joining across multiple tables (e.g. `appointment_details`, `prescription_item_details`) and 1 aggregate view (`monthly_revenue_by_department`) using `GROUP BY`, `DATE_TRUNC`, and `SUM`.
- **Sample data:** inserted across all 11 tables in correct foreign-key dependency order, deliberately including edge cases (optional fields left `NULL`, a patient with multiple appointments, a prescription with multiple medicines) to exercise the constraints and views with realistic data.
- **Constraint testing:** deliberately inserted invalid data (duplicate unique values, invalid foreign keys, out-of-range values, missing required fields) to confirm every constraint actually rejects bad data, not just exists on paper.

## SQL Practice

`sql/queries.sql` contains business-scenario SQL queries — each answering a realistic question a hospital staff member might ask (e.g. "Which doctor has the highest workload this month?", "Which patients have an invoice but haven't paid yet?"), rather than generic "list all rows" exercises.

Example:
```sql
-- Which patients have an invoice but have never made a payment?
SELECT p.full_name, p.identity_number
FROM invoice i
JOIN medical_record mr ON mr.medical_record_id = i.medical_record_id
JOIN appointment a ON a.appointment_id = mr.appointment_id
JOIN patient p ON p.patient_id = a.patient_id
WHERE NOT EXISTS (
    SELECT 1 FROM payment pm WHERE pm.invoice_id = i.invoice_id
);
```

Techniques covered so far: multi-table JOINs (including transitive joins through 5+ tables), `GROUP BY` with aggregates, `RANK() OVER` window functions for correctly handling ties in "top N" queries, correlated subqueries (`NOT EXISTS`), and date arithmetic (`AGE`, `EXTRACT`, `INTERVAL`, `DATE_TRUNC`).

## Roadmap Progress

| Phase | Status |
|---|---|
| Requirement Engineering | ✅ Done |
| Business Analysis | ✅ Done |
| Database Design (ERD, Normalization, Physical Design) | ✅ Done |
| Database Implementation (Constraints, Indexes, Views, Sample Data, Testing) | ✅ Done |
| SQL Practice (target: 40–60 queries) | 🚧 In Progress — 10 queries done |
| Documentation | 🚧 In Progress — this README |
| ETL / Data Warehouse / Star Schema | ⬜ Not started |

## Lessons Learned

- Designing constraints in the correct order (`NOT NULL` → `UNIQUE` → `CHECK` → `DEFAULT`) across all tables at once, rather than table-by-table, made it much easier to stay consistent and catch cross-table inconsistencies (e.g. same-purpose columns using different `VARCHAR` lengths).
- A foreign key alone does not enforce a 1:1 relationship — it only checks that the referenced row exists, not that it hasn't already been used elsewhere. A 1:1 relationship needs `FOREIGN KEY` + `UNIQUE` together on the child table.
- `DATE_TRUNC()` on a column disables index usage on that column (the index is sorted by the raw value, not the computed one), while a range query (`>=` / `<`) can use the index — a real trade-off between readability and performance, not just a style choice.
- Sample data should be written to deliberately exercise edge cases already reasoned about during design (e.g. a patient with two appointments on different days, to confirm why `appointment_id` needed to be a surrogate key rather than a composite key) — not just filled in for volume.