-- Migration : V002
-- Description : create Department Table 
-- Author : Xuan Hai 
-- Date : 2026-08-14

CREATE TABLE department (
    department_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_name VARCHAR(50),
    description TEXT,
    location VARCHAR(100),
    phone_number VARCHAR(10),
    department_status VARCHAR(20)
)