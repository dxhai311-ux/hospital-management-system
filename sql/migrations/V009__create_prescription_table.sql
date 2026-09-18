-- Migration : V009
-- Description : Create Prescription Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE prescription (
    prescription_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    medical_record_id INT REFERENCES medical_record(medical_record_id),
    prescribed_date DATE,
    instructions TEXT,
    prescription_status VARCHAR(20)
)