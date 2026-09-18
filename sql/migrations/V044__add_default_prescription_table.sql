-- Migration : V044
-- Description : Add default prescription table
-- Author : Xuan Hai
-- Date : 2026-08-16

ALTER TABLE prescription
    ALTER COLUMN prescription_status SET DEFAULT 'Issued';