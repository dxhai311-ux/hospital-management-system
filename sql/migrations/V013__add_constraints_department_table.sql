-- Migration : V013
-- Description : Add Constraints to Department Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE department
    ALTER COLUMN department_name SET NOT NULL,
    ALTER COLUMN location SET NOT NULL,
    ALTER COLUMN phone_number SET NOT NULL,
    ALTER COLUMN department_status SET NOT NULL;