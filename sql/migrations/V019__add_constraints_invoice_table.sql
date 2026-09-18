-- Migration : V019
-- Description : Add Constraints to Invoice Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE invoice
    ALTER COLUMN medical_record_id SET NOT NULL,
    ALTER COLUMN total_amount SET NOT NULL,
    ALTER COLUMN issued_date SET NOT NULL,
    ALTER COLUMN invoice_status SET NOT NULL;