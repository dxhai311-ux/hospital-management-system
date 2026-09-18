-- Migration : V021
-- Description : Add Constraints to Payment Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE payment
    ALTER COLUMN invoice_id SET NOT NULL,
    ALTER COLUMN payment_date SET NOT NULL,
    ALTER COLUMN payment_method SET NOT NULL,
    ALTER COLUMN payment_amount SET NOT NULL,
    ALTER COLUMN payment_status SET NOT NULL;