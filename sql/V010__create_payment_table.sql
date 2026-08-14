-- Migration : V010
-- Description : Create Payment Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE payment (
    payment_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    invoice_id INT REFERENCES invoice(invoice_id),
    payment_method VARCHAR(20),
    payment_date DATE,
    payment_amount DECIMAL(12, 2),
    payment_status VARCHAR(20),
    transaction_reference VARCHAR(50)
)