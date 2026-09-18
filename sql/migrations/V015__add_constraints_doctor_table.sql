-- Migration : V015
-- Description : Add Constraints to Doctor Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE doctor
    ALTER COLUMN full_name SET NOT NULL,
    ALTER COLUMN date_of_birth SET NOT NULL,
    ALTER COLUMN gender SET NOT NULL,
    ALTER COLUMN phone_number SET NOT NULL,
    ALTER COLUMN work_email SET NOT NULL,
    ALTER COLUMN specialty SET NOT NULL,
    ALTER COLUMN consultation_fee SET NOT NULL,
    ALTER COLUMN department_id SET NOT NULL,
    ALTER COLUMN license_number SET NOT NULL,
    ALTER COLUMN hire_date SET NOT NULL,
    ALTER COLUMN employment_status SET NOT NULL;