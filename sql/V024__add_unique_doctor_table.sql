-- Migration : V024
-- Description : Add Unique Constraint to Doctor Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE doctor
    ADD CONSTRAINT uq_doctor_work_email UNIQUE (work_email),
    ADD CONSTRAINT uq_doctor_license_number UNIQUE (license_number);