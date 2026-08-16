-- Migration : V045
-- Description : Add default invoice table
-- Author : Xuan Hai
-- Date : 2026-08-16

ALTER TABLE invoice
    ALTER COLUMN invoice_status SET DEFAULT 'Unpaid';