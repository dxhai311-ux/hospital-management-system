-- Migration : V036
-- Description : Add check prescription_item table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE prescription_item
    ADD CONSTRAINT chk_prescription_item_quantity CHECK (quantity > 0);