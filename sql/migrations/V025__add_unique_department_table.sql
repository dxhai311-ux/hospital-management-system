-- Migration : V025
-- Description : Add Unique Constraint to Department Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE department
    ADD CONSTRAINT uq_department_department_name UNIQUE (department_name);