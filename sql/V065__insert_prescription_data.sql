-- Migration : V066
-- Description : Insert sample data into prescription table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO prescription (medical_record_id, prescribed_date, instructions)
VALUES 
    (1, '2026-08-20', 'Uống sau ăn, tránh vận động mạnh'),
    (2, '2026-08-21', NULL);