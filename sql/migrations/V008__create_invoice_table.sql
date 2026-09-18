-- Migration : V008
-- Description : Create Invoice Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE invoice (
    invoice_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    medical_record_id INT REFERENCES medical_record(medical_record_id),
    total_amount DECIMAL(12, 2),
    issued_date DATE,
    invoice_status VARCHAR(20)
)