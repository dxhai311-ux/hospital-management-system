-- Migration : V031
-- Description : Add check medicine table
-- Author : Xuan Hai
-- Date : 2026-08-15

ALTER TABLE medicine 
    ADD CONSTRAINT chk_medicine_stock_quantity CHECK (stock_quantity >= 0),
    ADD CONSTRAINT chk_medicine_unit_price CHECK (unit_price > 0),
    ADD CONSTRAINT chk_medicine_manufacturer_befor_expiry CHECK (manufacture_date < expiry_date);