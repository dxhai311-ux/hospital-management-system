-- Migration :  V001
-- Description : Create Patient Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE patient (
    patient_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(20),
    phone_number VARCHAR(10),
    address VARCHAR(254),
    identity_number VARCHAR(12),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(10)
)