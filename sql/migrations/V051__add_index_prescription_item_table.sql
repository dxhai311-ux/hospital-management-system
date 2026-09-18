-- Migration : V051
-- Description : Add index to prescription_item table
-- Author : Xuan Hai
-- Date : 2026-08-16

CREATE INDEX idx_prescription_item_prescription_id ON prescription_item (prescription_id);
CREATE INDEX idx_prescription_item_medicine_id ON prescription_item (medicine_id);