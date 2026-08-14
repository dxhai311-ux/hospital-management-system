-- Migration : V018
-- Description : Add Constraints to Medical Record Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE medical_record
    ALTER COLUMN appointment_id SET NOT NULL,
    ALTER COLUMN diagnosis SET NOT NULL,
    ALTER COLUMN record_date SET NOT NULL;