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

-- Q6: Bệnh nhân nào chưa từng thanh toán bất kỳ hóa đơn nào (dù đã có hóa đơn được tạo)?
--     Lấy tên bệnh nhân và mã CCCD.
SELECT 
	p.full_name,
	p.identity_number
FROM invoice i
JOIN medical_record mr ON mr.medical_record_id = i.medical_record_id 
JOIN appointment a ON a.appointment_id = mr.appointment_id 
JOIN patient p ON p.patient_id = a.patient_id 
WHERE NOT EXISTS (
	SELECT 1 FROM payment pm
	WHERE pm.invoice_id = i.invoice_id
);
-- Note : NOT EXISTS để kiểm tra tồn tại/ không tồn tại? . Subquery duyệt từng dòng trong bảng invoice để đối chiếu với bảng payment

-- Q7: Trong số các bệnh nhân đã có lịch hẹn, ai là người lớn tuổi nhất?
--     Lấy tên, ngày sinh, và tuổi hiện tại (tính bằng số nguyên, đơn vị năm).
SELECT
	full_name,
	date_of_birth,
	age
FROM (	
	SELECT DISTINCT
		p.full_name,
		p.date_of_birth,
		EXTRACT(YEAR FROM AGE(p.date_of_birth)) AS age,
		RANK() OVER (ORDER BY EXTRACT(YEAR FROM AGE(p.date_of_birth)) DESC) AS rank
	FROM appointment a
	JOIN patient p ON p.patient_id = a.patient_id 
) ranked
WHERE rank = 1;

-- Q8: Trong danh sách thuốc hiện có trong kho, thuốc nào sắp hết hạn trong vòng 6 tháng tới (tính từ hôm nay)?
--     Lấy tên thuốc, ngày hết hạn, và số lượng tồn kho.
SELECT 
	medicine_name, 
	expiry_date,
	stock_quantity
FROM medicine
WHERE CURRENT_DATE + INTERVAL '6 months' > expiry_date AND CURRENT_DATE < expiry_date;

-- Q9: Trong tất cả các bác sĩ, ai có thu nhập từ phí khám cao nhất trong tháng 8/2026?
--     Lấy tên bác sĩ và tổng thu nhập ước tính.
SELECT 
	d.doctor_id,
	d.full_name,
	d.consultation_fee * COUNT(a.appointment_id) AS total
FROM doctor d
JOIN appointment a ON d.doctor_id = a.doctor_id
WHERE DATE_TRUNC('month', a.appointment_date) = '2026-08-01' AND a.appointment_status = 'Completed' 
GROUP BY d.doctor_id, d.full_name, d.consultation_fee 
ORDER BY total DESC
LIMIT 1;

-- Q10: Trong tất cả các khoa, khoa nào có nhiều bác sĩ nhất?
--      Lấy tên khoa và số lượng bác sĩ. Nếu có nhiều khoa hòa nhau về số lượng cao nhất, hiển thị tất cả các khoa đó
SELECT department_name, doctor_count, rank
FROM (
    SELECT 
        dep.department_name,
        COUNT(d.doctor_id) AS doctor_count,
        RANK() OVER (ORDER BY COUNT(d.doctor_id) DESC) AS rank
    FROM department dep
    JOIN doctor d ON dep.department_id = d.department_id
    GROUP BY dep.department_name
) ranked
WHERE rank = 1;