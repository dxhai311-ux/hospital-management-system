-- Migration : V023
-- Description : Add Unique Constraint to Patient Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE patient
    ADD CONSTRAINT uq_patient_identity_number UNIQUE (identity_number);