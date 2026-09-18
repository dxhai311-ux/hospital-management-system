-- Migration : V022
-- Description : Add Constraints to Prescription Item Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE prescription_item
    ALTER COLUMN prescription_id SET NOT NULL,
    ALTER COLUMN medicine_id SET NOT NULL,
    ALTER COLUMN quantity SET NOT NULL,
    ALTER COLUMN dosage SET NOT NULL,
    ALTER COLUMN frequency SET NOT NULL,
    ALTER COLUMN duration SET NOT NULL;