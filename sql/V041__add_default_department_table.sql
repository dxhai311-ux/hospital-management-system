-- Migration : V041
-- Description : Add default department table
-- Author : Xuan Hai
-- Date : 2026-08-16

ALTER TABLE department
    ALTER COLUMN department_status SET DEFAULT 'Active';