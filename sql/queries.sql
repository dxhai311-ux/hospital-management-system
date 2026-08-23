-- SQL Practice Queries
-- Phase 5 — Hospital Management System
-- Author : Xuan Hai
-- Format: Mỗi câu SQL trả lời 1 câu hỏi nghiệp vụ thực tế

-- =======================================================

-- Q1: Mỗi bác sĩ khoa Tim mạch hiện có bao nhiêu lịch hẹn đã lên lịch (Scheduled)?
SELECT 
    d.doctor_id,
    d.full_name AS doctor_name,
    COUNT(a.appointment_id) AS total_appointments
FROM doctor d
JOIN appointment a ON d.doctor_id = a.doctor_id
WHERE d.specialty = 'Tim mạch' AND a.appointment_status = 'Scheduled'
GROUP BY d.doctor_id, d.full_name;

-- Q2: Tổng số tiền bệnh viện đã thực sự thu được (đã thanh toán) tính đến hiện tại?
SELECT 
    COALESCE(SUM(payment_amount), 0) AS total_revenue
FROM payment
WHERE payment_status = 'Successful';
-- Note: Nếu không có dòng nào khớp thì sum() sẽ trả về NULL, không phải 0

-- Q3: Bệnh nhân nào đã đặt lịch hẹn nhiều nhất từ trước tới nay?
SELECT 
    patient_id,
    patient_name,
    total_appointments
FROM (
    SELECT 
        p.patient_id,
        p.full_name AS patient_name,
        COUNT(a.appointment_id) AS total_appointments,
        RANK() OVER (ORDER BY COUNT(a.appointment_id) DESC) AS rank
    FROM appointment a
    JOIN patient p ON a.patient_id = p.patient_id
    GROUP BY p.patient_id, p.full_name
) ranked
WHERE rank = 1

-- Q4: Trong tháng 8/2026, mỗi khoa có bao nhiêu lượt khám (appointment)?
--     Sắp xếp khoa có nhiều lượt khám nhất lên đầu.
SELECT 
    dep.department_name AS department_name, 
    COUNT(*) AS total_appointments
FROM appointment a
JOIN doctor d ON a.doctor_id = d.doctor_id
JOIN department dep ON d.department_id = dep.department_id
WHERE a.appointment_date >= '2026-08-01' AND a.appointment_date < '2026-09-01'
GROUP BY dep.department_name
ORDER BY total_appointments DESC;
-- Note : Cách 2 dùng DATE_TRUNC nhưng sẽ không áp dụng được index

-- Q5: Loại thuốc nào được kê nhiều nhất (tính theo tổng số lượng đã kê trong tất cả đơn thuốc)? 
--     Lấy tên thuốc và tổng số lượng.
SELECT 
    medicine_id,
    medicine_name,
    total_quantity
FROM (
    SELECT
        pi.medicine_id,
        m.medicine_name AS medicine_name,
        SUM(pi.quantity) AS total_quantity,
        RANK() OVER (ORDER BY SUM(pi.quantity) DESC) AS rank
    FROM medicine m
    JOIN prescription_item pi ON m.medicine_id = pi.medicine_id
    GROUP BY pi.medicine_id, m.medicine_name
) ranked
WHERE rank = 1;