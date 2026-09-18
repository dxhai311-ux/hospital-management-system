-- Migration : V012
-- Description : Add Constraints to Patient Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE patient
    ALTER COLUMN full_name SET NOT NULL,
    ALTER COLUMN date_of_birth SET NOT NULL,
    ALTER COLUMN gender SET NOT NULL,
    ALTER COLUMN phone_number SET NOT NULL,
    ALTER COLUMN address SET NOT NULL;