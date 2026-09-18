-- Migration : V056
-- Description : Create view monthly revenue by department
-- Author : Xuan Hai
-- Date : 2026-08-17

CREATE VIEW monthly_revenue_by_department AS
SELECT 
    dep.department_name AS department_name,
    DATE_TRUNC('month', i.issued_date) AS month,
    SUM(i.total_amount) AS revenue
FROM invoice i 
JOIN medical_record mr ON i.medical_record_id = mr.medical_record_id
JOIN appointment a ON mr.appointment_id = a.appointment_id
JOIN doctor d ON a.doctor_id = d.doctor_id
JOIN department dep ON d.department_id = dep.department_id
WHERE i.invoice_status = 'Paid'
GROUP BY dep.department_name, DATE_TRUNC('month', i.issued_date);