-- Migration : V050
-- Description : Add index to prescription table
-- Author : Xuan Hai
-- Date : 2026-08-16

CREATE INDEX idx_prescription_medical_record_id ON prescription (medical_record_id);