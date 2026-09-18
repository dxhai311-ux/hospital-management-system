-- Migration : V060
-- Description : Insert sample data into medicine table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO medicine (medicine_name, active_ingredient, unit, strength, manufacturer, manufacture_date, expiry_date, stock_quantity, unit_price)
VALUES 
    ('Paracetamol', 'Paracetamol', 'Tablet', '500mg', 'Traphaco', '2026-01-10', '2028-01-10', 500, 2000.00),
    ('Amoxicillin', 'Amoxicillin', 'Capsule', '250mg', 'DHG Pharma', '2026-02-15', '2027-08-15', 300, 5000.00),
    ('Vitamin C', 'Ascorbic Acid', 'Tablet', '1000mg', 'Imexpharm', '2026-03-01', '2028-03-01', 800, 3000.00),
    ('Ibuprofen', 'Ibuprofen', 'Tablet', '400mg', 'Traphaco', '2026-01-20', '2027-07-20', 400, 4500.00);