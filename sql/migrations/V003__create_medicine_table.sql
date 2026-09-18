-- Migration : V003
-- Description : Create Medicine Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE medicine (
    medicine_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    medicine_name VARCHAR(50),
    active_ingredient VARCHAR(100),
    unit VARCHAR(20),
    strength VARCHAR(20),
    manufacturer VARCHAR(50),
    manufacture_date DATE,
    expiry_date DATE,
    stock_quantity INT,
    unit_price DECIMAL(10, 2),
    medicine_status VARCHAR(20)
)