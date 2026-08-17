-- Migration : V053
-- Description : Create view medical record details
-- Author : Xuan Hai
-- Date : 2026-08-17

CREATE VIEW medical_record_details AS
SELECT 
    p.full_name AS patient_name,
    d.full_name AS doctor_name,
    mr.diagnosis AS diagnosis,
    mr.symptoms AS symptoms,
    mr.treatment AS treatment,
    mr.record_date AS record_date
FROM medical_record mr 
JOIN appointment a ON mr.appointment_id = a.appointment_id
JOIN patient p ON a.patient_id = p.patient_id
JOIN doctor d ON a.doctor_id = d.doctor_id;