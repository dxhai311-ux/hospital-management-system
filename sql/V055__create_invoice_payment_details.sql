-- Migration : V055
-- Description : Create view invoice payment details
-- Author : Xuan Hai
-- Date : 2026-08-17

CREATE VIEW invoice_payment_details AS
SELECT 
    p.full_name AS patient_name, 
    p.identity_number AS patient_identity_number,
    i.total_amount AS invoice_total_amount,
    i.invoice_status AS invoice_status,
    pay.payment_method AS payment_method,
    pay.payment_amount AS payment_amount,
    pay.payment_status AS payment_status
FROM payment pay
JOIN invoice i ON pay.invoice_id = i.invoice_id
JOIN medical_record mr ON i.medical_record_id = mr.medical_record_id
JOIN appointment a ON mr.appointment_id = a.appointment_id
JOIN patient p ON a.patient_id = p.patient_id;