-- Migration : V034
-- Description : Add check date of birth doctor table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE doctor 
    ADD CONSTRAINT chk_doctor_date_of_birth CHECK (date_of_birth < CURRENT_DATE);