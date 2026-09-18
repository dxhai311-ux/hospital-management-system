-- Migration : V014
-- Description : Add Constraints to Medicine Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE medicine 
    ALTER COLUMN medicine_name SET NOT NULL,
    ALTER COLUMN active_ingredient SET NOT NULL,
    ALTER COLUMN unit SET NOT NULL,
    ALTER COLUMN strength SET NOT NULL,
    ALTER COLUMN manufacturer SET NOT NULL,
    ALTER COLUMN manufacture_date SET NOT NULL,
    ALTER COLUMN expiry_date SET NOT NULL,
    ALTER COLUMN stock_quantity SET NOT NULL,
    ALTER COLUMN unit_price SET NOT NULL,
    ALTER COLUMN medicine_status SET NOT NULL;