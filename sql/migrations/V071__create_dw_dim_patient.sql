-- Migration : V071
-- Description : Create table dim_patient in dw
-- Author : Xuan Hai
-- Date : 2026-11-28

CREATE TABLE dw.dim_patient (
    patient_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    patient_id INT UNIQUE NOT NULL,
    full_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(20)
);