-- Migration : V033
-- Description : Add check patient table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE patient 
    ADD CONSTRAINT chk_patient_date_of_birth CHECK (date_of_birth < CURRENT_DATE);