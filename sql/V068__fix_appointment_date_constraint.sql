-- Migration : V068
-- Description : Fix appointment date constraint
-- Author : Xuan Hai
-- Date : 2026-09-17

ALTER TABLE appointment
    DROP CONSTRAINT chk_appointment_date;

ALTER TABLE appointment
    ADD CONSTRAINT chk_appointment_date CHECK (appointment_date >= '2020-01-01');