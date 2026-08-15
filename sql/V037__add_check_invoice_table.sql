-- Migration : V037
-- Description : Add check invoice table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE invoice 
    ADD CONSTRAINT chk_invoice_total_amount CHECK (total_amount > 0);