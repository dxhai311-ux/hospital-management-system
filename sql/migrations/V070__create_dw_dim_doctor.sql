-- Migration : V070
-- Description : Create table dim_doctor in dw
-- Author : Xuan Hai
-- Date : 2026-11-28

CREATE TABLE dw.dim_doctor (
    doctor_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    doctor_id INT UNIQUE NOT NULL,
    full_name VARCHAR(100),
    gender VARCHAR(20),
    specialty VARCHAR(100),
    employment_status VARCHAR(20)
);