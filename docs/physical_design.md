# Physical Database Design

## Overview

This document defines the concrete PostgreSQL data type for every column across all 11 entities, based on the Logical ERD (`diagrams/logical_erd.drawio`) and the Normalization Analysis (`docs/normalization.md`).

**Target DBMS:** PostgreSQL
**Client tool:** DBeaver (GUI only — does not affect SQL syntax)

This document is the direct input for Buổi 9 (CREATE TABLE statements).

---

## Design Conventions

- **Primary keys:** `INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY` for all entities. `INT` (max ~2.1 billion) is sufficient for a single-hospital, single-branch system (per `requirement.md` Assumptions). `BIGINT`/`UUID` are not needed at this scale.
- **Foreign keys:** always the same data type as the primary key they reference (`INT`).
- **Money columns:** `DECIMAL(m,n)`, never `FLOAT`, to avoid floating-point rounding errors. `n = 2` (VND has no sub-unit). `m` sized with a safety margin above realistic maximums (see reasoning below).
- **Status columns:** `VARCHAR(20)` rather than `ENUM`. `ENUM` would enforce valid values at the DB level, but requires `ALTER TABLE` to add a new status later. `VARCHAR` + application-level validation is more flexible for a system still evolving.
- **Free-form clinical/descriptive text** (diagnosis, symptoms, treatment, notes, instructions, description): `TEXT` — no predictable length limit.
- **Short structured text with a predictable bound** (name, phone, dosage instructions, license number): `VARCHAR(n)` — length chosen with a reasonable safety margin over realistic real-world values.
- **Identifiers that look numeric but may contain letters/leading zeros** (phone number, identity number, license number): always `VARCHAR`, never `INT` — these values are never used in arithmetic.

---

## 1. Patient

| Column | Type |
|---|---|
| patient_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| full_name | VARCHAR(100) |
| date_of_birth | DATE |
| gender | VARCHAR(20) |
| phone_number | VARCHAR(10) |
| address | VARCHAR(254) |
| identity_number | VARCHAR(12) |
| emergency_contact_name | VARCHAR(100) |
| emergency_contact_phone | VARCHAR(10) |

## 2. Doctor

| Column | Type |
|---|---|
| doctor_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| full_name | VARCHAR(100) |
| date_of_birth | DATE |
| gender | VARCHAR(20) |
| phone_number | VARCHAR(10) |
| work_email | VARCHAR(254) |
| specialty | VARCHAR(100) |
| consultation_fee | DECIMAL(10,2) |
| department_id | INT REFERENCES Department(department_id) |
| license_number | VARCHAR(50) |
| hire_date | DATE |
| employment_status | VARCHAR(20) |

## 3. Department

| Column | Type |
|---|---|
| department_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| department_name | VARCHAR(50) |
| description | TEXT |
| location | VARCHAR(254) |
| phone_number | VARCHAR(10) |
| department_status | VARCHAR(20) |

## 4. Room

| Column | Type |
|---|---|
| room_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| room_name | VARCHAR(50) |
| room_type | VARCHAR(50) |
| department_id | INT REFERENCES Department(department_id) |
| capacity | INT |
| location | VARCHAR(100) |
| room_status | VARCHAR(20) |

## 5. Appointment

| Column | Type |
|---|---|
| appointment_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| patient_id | INT REFERENCES Patient(patient_id) |
| doctor_id | INT REFERENCES Doctor(doctor_id) |
| appointment_date | DATE |
| appointment_time | TIME |
| room_id | INT REFERENCES Room(room_id) |
| reason | TEXT |
| appointment_status | VARCHAR(20) |

## 6. Medical_Record

| Column | Type |
|---|---|
| medical_record_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| appointment_id | INT REFERENCES Appointment(appointment_id) |
| diagnosis | TEXT |
| symptoms | TEXT |
| treatment | TEXT |
| notes | TEXT |
| record_date | DATE |

## 7. Prescription

| Column | Type |
|---|---|
| prescription_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| medical_record_id | INT REFERENCES Medical_Record(medical_record_id) |
| prescribed_date | DATE |
| instructions | TEXT |
| prescription_status | VARCHAR(20) |

## 8. Prescription_Item

| Column | Type |
|---|---|
| prescription_item_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| prescription_id | INT REFERENCES Prescription(prescription_id) |
| medicine_id | INT REFERENCES Medicine(medicine_id) |
| quantity | INT |
| dosage | VARCHAR(50) |
| frequency | VARCHAR(50) |
| duration | VARCHAR(50) |

## 9. Medicine

| Column | Type |
|---|---|
| medicine_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| medicine_name | VARCHAR(50) |
| active_ingredient | VARCHAR(100) |
| unit | VARCHAR(20) |
| strength | VARCHAR(20) |
| manufacturer | VARCHAR(50) |
| manufacture_date | DATE |
| expiry_date | DATE |
| stock_quantity | INT |
| unit_price | DECIMAL(10,2) |
| medicine_status | VARCHAR(20) |

## 10. Invoice

| Column | Type |
|---|---|
| invoice_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| medical_record_id | INT REFERENCES Medical_Record(medical_record_id) |
| total_amount | DECIMAL(12,2) |
| issued_date | DATE |
| invoice_status | VARCHAR(20) |

## 11. Payment

| Column | Type |
|---|---|
| payment_id | INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY |
| invoice_id | INT REFERENCES Invoice(invoice_id) |
| payment_method | VARCHAR(20) |
| payment_date | DATE |
| payment_amount | DECIMAL(12,2) |
| payment_status | VARCHAR(20) |
| transaction_reference | VARCHAR(50) |

---

## Notable Decisions

- **`consultation_fee` and `unit_price`/`total_amount`/`payment_amount` use different `DECIMAL(m,n)` precision** (`10,2` vs `12,2`): a single invoice can sum multiple medicines plus a consultation fee, so its maximum realistic value is larger than any single fee or unit price. `m` was chosen with a safety margin, not an exact calculated maximum.
- **`unit` and `strength` in Medicine are `VARCHAR`, not numeric**, because their values combine a number and a unit as one string (e.g. `"500mg"`, `"Tablet"`) — storing them as `INT` would silently drop the unit.
- **`dosage`, `frequency`, `duration` in Prescription_Item are `VARCHAR(50)`, not `TEXT`**: although free-text, their realistic values are always short phrases (e.g. "1 tablet", "2 times/day", "7 days"), so a bounded length better documents the expected data than an unbounded `TEXT`.
