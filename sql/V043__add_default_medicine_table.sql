-- Migration : V043
-- Description : Add default medicine table
-- Author : Xuan Hai
-- Date : 2026-08-16

ALTER TABLE medicine
    ALTER COLUMN medicine_status SET DEFAULT 'Active';