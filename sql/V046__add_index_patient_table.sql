-- Migration : V046
-- Description : Add index to patient table
-- Author : Xuan Hai
-- Date : 2026-08-16

CREATE INDEX idx_patient_phone_number ON patient (phone_number);