-- Migration : V035
-- Description : Add check appointment table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE appointment 
    ADD CONSTRAINT chk_appointment_date CHECK (appointment_date >= CURRENT_DATE);