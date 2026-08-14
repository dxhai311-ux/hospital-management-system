-- Migration : V011
-- Description : Create Prescription Item Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE prescription_item (
    prescription_item_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    prescription_id INT REFERENCES prescription(prescription_id),
    medicine_id INT REFERENCES medicine(medicine_id),
    quantity INT,
    dosage VARCHAR(50),
    frequency VARCHAR(50),
    duration VARCHAR(50)
)