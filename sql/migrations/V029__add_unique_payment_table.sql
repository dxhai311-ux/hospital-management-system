-- Migration : V029
-- Description : Add Unique Constraint to Payment Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE payment
    ADD CONSTRAINT uq_payment_invoice_id UNIQUE (invoice_id);