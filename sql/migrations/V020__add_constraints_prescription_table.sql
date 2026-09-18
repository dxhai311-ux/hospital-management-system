-- Migration : V020 
-- Description : Add Constraints to Prescription Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE prescription
    ALTER COLUMN medical_record_id SET NOT NULL,
    ALTER COLUMN prescribed_date SET NOT NULL,
    ALTER COLUMN prescription_status SET NOT NULL;