-- Migration : V007
-- Description : Create Medical Record Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE medical_record (
    medical_record_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    appointment_id INT REFERENCES appointment(appointment_id),
    diagnosis TEXT,
    symptoms TEXT,
    treatment TEXT,
    notes TEXT,
    record_date DATE
)