-- Migration : V069
-- Description : Create table dim_department in dw
-- Author : Xuan Hai
-- Date : 2026-11-27

CREATE TABLE dw.dim_department(
    department_key INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_id INT UNIQUE NOT NULL,
    department_name VARCHAR(100),
    location VARCHAR(100),
    department_status VARCHAR(20)
);