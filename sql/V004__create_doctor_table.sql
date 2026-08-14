-- Migration : v004
-- Description : Create Doctor Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE doctor (
    doctor_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(20),
    phone_number VARCHAR(10),
    work_email VARCHAR(254),
    specialty VARCHAR(100),
    consultation_fee DECIMAL(10, 2),
    department_id INT REFERENCES department(department_id),
    license_number VARCHAR(50),
    hire_date DATE,
    employment_status VARCHAR(20)
)