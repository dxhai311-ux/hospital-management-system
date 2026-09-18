-- Migration : V027
-- Description : Add Unique Constraint to Medical Record Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE medical_record
    ADD CONSTRAINT uq_medical_record_appointment_id UNIQUE (appointment_id);