-- Migration : V062
-- Description : Insert sample data into room table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO room (room_name, room_type, department_id, capacity, location)
VALUES 
    ('101', 'Consultation Room', 1, 2, 'Tầng 2, Tòa A'),
    ('102', 'Consultation Room', 1, 2, 'Tầng 2, Tòa A'),
    ('101', 'Consultation Room', 2, 3, 'Tầng 1, Tòa A'),
    ('201', 'Consultation Room', 3, 2, 'Tầng 3, Tòa B'),
    ('301', 'Operating Room', 4, 6, 'Tầng 4, Tòa B');