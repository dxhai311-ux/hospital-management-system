-- Migration : V052
-- Description : Create view appointment details
-- Author : Xuan Hai
-- Date : 2026-08-17

CREATE VIEW appointment_details AS
SELECT 
    p.full_name AS patient_name,
    d.full_name AS doctor_name,
    r.room_name AS room_name,
    a.appointment_date AS appointment_date,
    a.appointment_time AS appointment_time,
    a.appointment_status AS appointment_status
FROM appointment a 
JOIN patient p ON a.patient_id = p.patient_id
JOIN doctor d ON a.doctor_id = d.doctor_id
JOIN room r ON a.room_id = r.room_id;