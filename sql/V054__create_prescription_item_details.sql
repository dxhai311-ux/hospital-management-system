-- Migration : V054
-- Description : Create view prescription item details
-- Author : Xuan Hai
-- Date : 2026-08-17

CREATE VIEW prescription_item_details AS
SELECT 
    pt.full_name AS patient_name, 
    pt.identity_number AS patient_identity_number,
    m.medicine_name AS medicine_name,
    pi.quantity AS quantity,
    pi.dosage AS dosage,
    pi.frequency AS frequency,
    pi.duration AS duration
FROM prescription_item pi 
JOIN medicine m ON pi.medicine_id = m.medicine_id
JOIN prescription p ON pi.prescription_id = p.prescription_id
JOIN medical_record mr ON p.medical_record_id = mr.medical_record_id
JOIN appointment a ON a.appointment_id = mr.appointment_id
JOIN patient pt ON a.patient_id = pt.patient_id;