-- Migration : V030
-- Description : Add check doctor table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE doctor 
    ADD CONSTRAINT chk_doctor_consultation_fee CHECK (consultation_fee > 0);