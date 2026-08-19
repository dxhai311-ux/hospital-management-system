-- Migration : V063
-- Description : Insert sample data into appointment table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO appointment (patient_id, doctor_id, appointment_date, appointment_time, room_id, reason)
VALUES 
    (1, 1, '2026-08-20', '08:30:00', 1, 'Đau ngực, khó thở'),
    (1, 1, '2026-09-05', '09:00:00', 1, 'Tái khám tim mạch'),
    (2, 2, '2026-08-21', '10:00:00', 3, 'Sốt kéo dài'),
    (3, 3, '2026-08-22', '14:00:00', 4, 'Khám sức khỏe định kỳ cho con'),
    (4, 4, '2026-08-25', '08:00:00', 5, 'Chuẩn bị phẫu thuật ruột thừa'),
    (5, 5, '2026-08-19', '11:00:00', 2, NULL);