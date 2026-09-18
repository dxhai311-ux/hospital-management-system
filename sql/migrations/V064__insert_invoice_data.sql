-- Migration : V065
-- Description : Insert sample data into invoice table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO invoice (medical_record_id, total_amount, issued_date, invoice_status)
VALUES 
    (1, 350000.00, '2026-08-20', 'Paid'),
    (2, 220000.00, '2026-08-21', 'Unpaid'),
    (3, 250000.00, '2026-08-22', 'Paid');