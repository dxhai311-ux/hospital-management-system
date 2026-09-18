-- Migration : V038
-- Description : Add check payment table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE payment 
    ADD CONSTRAINT chk_payment_amount CHECK (payment_amount > 0);