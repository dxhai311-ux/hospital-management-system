-- Migration : V039
-- Description : Add default appointment table
-- Author : Xuan Hai
-- Date : 2026-08-16

ALTER TABLE appointment
    ALTER COLUMN appointment_status SET DEFAULT 'Scheduled';