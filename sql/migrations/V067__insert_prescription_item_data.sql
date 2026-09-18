-- Migration : V068
-- Description : Insert sample data into prescription_item table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO prescription_item (prescription_id, medicine_id, quantity, dosage, frequency, duration)
VALUES 
    (1, 1, 14, '1 viên', '2 lần/ngày', '7 ngày'),
    (1, 3, 10, '1 viên', '1 lần/ngày', '10 ngày'),
    (2, 2, 21, '1 viên', '3 lần/ngày', '7 ngày');