-- Migration : V028
-- Description : Add Unique Constraint to Invoice Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE invoice
    ADD CONSTRAINT uq_invoice_medical_record_id UNIQUE (medical_record_id);