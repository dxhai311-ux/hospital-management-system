-- Migration : V048
-- Description : Add index to medicine table
-- Author : Xuan Hai
-- Date : 2026-08-16

CREATE INDEX idx_medicine_name ON medicine (medicine_name);
CREATE INDEX idx_medicine_active_ingredient ON medicine (active_ingredient);