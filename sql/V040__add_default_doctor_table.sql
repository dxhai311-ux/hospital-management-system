-- Migration : V040
-- Description : Add default doctor table
-- Author : Xuan Hai
-- Date : 2026-08-16

ALTER TABLE doctor 
    ALTER COLUMN employment_status SET DEFAULT 'Active';