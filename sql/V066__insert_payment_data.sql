-- Migration : V067
-- Description : Insert sample data into payment table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO payment (invoice_id, payment_method, payment_date, payment_amount, payment_status)
VALUES 
    (1, 'Cash', '2026-08-20', 350000.00, 'Successful'),
    (3, 'Bank Transfer', '2026-08-22', 250000.00, 'Successful');