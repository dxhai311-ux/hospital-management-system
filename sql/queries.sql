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
WHERE rank = 1;

-- Q4: Trong tháng 8/2026, mỗi khoa có bao nhiêu lượt khám (appointment)?
--     Sắp xếp khoa có nhiều lượt khám nhất lên đầu.
SELECT dep.department_name, COUNT(a.appointment_id) AS total
FROM department dep
LEFT JOIN doctor d ON d.department_id = dep.department_id
LEFT JOIN appointment a ON a.doctor_id = d.doctor_id
                       AND a.appointment_date >= '2026-08-01'
                       AND a.appointment_date <  '2026-09-01'
GROUP BY dep.department_name
ORDER BY total DESC;

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
JOIN medical_record mr ON i.medical_record_id = mr.medical_record_id
JOIN appointment a ON mr.appointment_id = a.appointment_id 
JOIN patient p ON a.patient_id = p.patient_id 
GROUP BY p.patient_id
HAVING COUNT(CASE WHEN i.invoice_status = 'Paid' THEN 1 END) = 0;

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
WHERE a.appointment_date >= '2026-08-01' AND a.appointment_date < '2026-09-01' 
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

-- Q11: Những khoa nào hiện chưa có bác sĩ nào?
--      Lấy tên khoa, sắp xếp theo tên khoa.
SELECT dep.department_name
FROM department dep
LEFT JOIN doctor d ON dep.department_id = d.department_id 
WHERE d.doctor_id IS NULL
ORDER BY dep.department_name;

-- Q12: Những bệnh nhân nào bị đăng ký trùng(cùng họ tên, ngày sinh và số điện thoại)?
--      Lấy họ tên, ngày sinh, số điện thoại và số lần xuất hiện,
--      sắp xếp số lần xuất hiện giảm dần.
SELECT 
	full_name,
	date_of_birth,
	phone_number,
	COUNT(*) as occurrences
FROM patient
GROUP BY full_name, date_of_birth, phone_number
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;

-- Q13: Những bác sĩ nào có số lịch hẹn đã hoàn thành (Completed)
--      nhiều hơn mức trung bình của tất cả bác sĩ?
--      Lấy mã bác sĩ, tên bác sĩ và số lịch Completed,
--      sắp xếp số lịch giảm dần.
WITH cte AS (
	SELECT d.doctor_id, d.full_name, COUNT(*) AS completed_count
	FROM doctor d
	JOIN appointment a ON d.doctor_id = a.doctor_id
	WHERE a.appointment_status IN ('Completed', 'completed', 'Complete')
	GROUP BY d.doctor_id, d.full_name 
)
SELECT *
FROM cte
WHERE completed_count > (
	SELECT AVG(completed_count)
	FROM cte
)
ORDER BY completed_count DESC;

-- Q14: Với mỗi khoa, bác sĩ nào có nhiều lịch hẹn đã hoàn thành (Completed) nhất?
--      Lấy tên khoa, tên bác sĩ và số lịch Completed.
--      Nếu có nhiều bác sĩ đồng số lịch cao nhất trong cùng khoa, hiện tất cả bác sĩ đồng hạng đó.
WITH ranked AS (
	SELECT 
		dep.department_id,
		d.doctor_id,
		COUNT(*) AS completed_count,
		RANK() OVER (PARTITION BY dep.department_id ORDER BY COUNT(*) DESC) AS rank
	FROM department dep 
	JOIN doctor d ON dep.department_id = d.department_id 
	JOIN appointment a ON d.doctor_id = a.doctor_id 
	WHERE a.appointment_status IN ('Completed', 'completed', 'Complete')
	GROUP BY dep.department_id, d.doctor_id
)
SELECT 
	dep.department_name,
	d.full_name,
	completed_count
FROM ranked
JOIN doctor d ON ranked.doctor_id = d.doctor_id 
JOIN department dep ON dep.department_id = ranked.department_id
WHERE rank = 1;

-- Q15: Doanh thu theo từng tháng (chỉ tính hóa đơn đã thanh toán, status = 'Paid').
--      Lấy tháng, doanh thu tháng đó, doanh thu tháng trước,
--      và chênh lệch giữa hai tháng.
--      Sắp xếp theo tháng tăng dần.
WITH cte AS (
	SELECT 
		DATE_TRUNC('month', issued_date) AS month_year,
		SUM(total_amount) AS monthly_revenue
	FROM invoice 
	WHERE invoice_status = 'Paid'
	GROUP BY DATE_TRUNC('month', issued_date)
)
SELECT
	*,
	LAG(monthly_revenue) OVER (ORDER BY month_year) AS last_month,
	(monthly_revenue - LAG(monthly_revenue) OVER (ORDER BY month_year)) AS difference
FROM cte
ORDER BY month_year;

-- Q16: Doanh thu tích lũy theo từng tháng trong mỗi năm
--      (chỉ tính hóa đơn Paid, status = 'Paid').
--      Lấy năm, tháng, doanh thu tháng đó,
--      và doanh thu cộng dồn từ tháng 1 đến tháng đó trong cùng năm.
--      Sang năm mới thì cộng dồn bắt đầu lại từ đầu.
--      Sắp xếp theo năm, rồi tháng tăng dần.
WITH cte AS (
	SELECT 
		EXTRACT(YEAR FROM issued_date) AS year,
		EXTRACT(MONTH FROM issued_date) AS month,
		SUM(total_amount) AS monthly_revenue
	FROM invoice 
	WHERE invoice_status = 'Paid'
	GROUP BY EXTRACT(YEAR FROM issued_date), EXTRACT(MONTH FROM issued_date)
)
SELECT *,
	SUM(monthly_revenue) OVER (PARTITION BY year ORDER BY month) AS cumulative_revenue
FROM cte 
ORDER BY year, month;

-- Q17: Những bệnh nhân nào đã từng đặt lịch nhưng chưa bao giờ có
--      lịch hẹn nào ở trạng thái Completed?
--      Lấy mã bệnh nhân, họ tên và tổng số lịch hẹn của họ.
--      Sắp xếp theo tổng số lịch giảm dần.
SELECT 
	p.patient_id,
	p.full_name, 
	COUNT(*) AS total_appointment
FROM appointment a
JOIN patient p ON a.patient_id = p.patient_id 
GROUP BY p.patient_id
HAVING COUNT(CASE WHEN LOWER(appointment_status) IN ('completed', 'complete') THEN 1 END) = 0
ORDER BY total_appointment DESC; 

-- Q18: Top 5 loại thuốc được kê nhiều nhất (theo tổng số lượng).
--      Lấy tên thuốc, tổng số lượng đã kê,
--      và số đơn thuốc khác nhau có chứa thuốc đó.
--      Sắp xếp theo tổng số lượng giảm dần.
SELECT 
	pi.medicine_id,
	m.medicine_name,
	SUM(quantity) AS total_quantity,
	COUNT(DISTINCT pi.prescription_id) AS prescription_count
FROM prescription_item pi 
JOIN medicine m ON m.medicine_id = pi.medicine_id 
GROUP BY pi.medicine_id, m.medicine_name
ORDER BY total_quantity DESC
LIMIT 5;

-- Q19: Với mỗi bác sĩ, tính tỷ lệ phần trăm lịch hẹn bị hủy (Cancelled).
--      Lấy tên bác sĩ, tổng số lịch, số lịch bị hủy và tỷ lệ hủy (%),
--      làm tròn 2 chữ số thập phân.
--      Chỉ lấy bác sĩ có từ 100 lịch hẹn trở lên.
--      Sắp xếp theo tỷ lệ hủy giảm dần.
WITH cte AS (
	SELECT 
		a.doctor_id,
		COUNT(a.appointment_id) AS appointment_count,
		COUNT(CASE WHEN a.appointment_status = 'Cancelled' THEN 1 END) AS appointment_cancelled
	FROM appointment a 
	GROUP BY a.doctor_id
	HAVING COUNT(a.appointment_id) >= 100
)
SELECT 
	d.full_name,
	cte.appointment_count,
	cte.appointment_cancelled,
	ROUND(appointment_cancelled::numeric / appointment_count * 100, 2) AS rate
FROM cte
JOIN doctor d ON cte.doctor_id = d.doctor_id
ORDER BY rate DESC;

-- Q20: Với mỗi năm, tìm 3 bệnh nhân có tổng số tiền đã thanh toán nhiều nhất.
--      Chỉ tính hóa đơn Paid, năm lấy theo ngày lập hóa đơn (issued_date).
--      Lấy năm, tên bệnh nhân, tổng tiền, và thứ hạng trong năm đó.
--      Nếu đồng hạng thì hiện tất cả bệnh nhân đồng hạng, dù ra hơn 3 người.
--      Sắp xếp theo năm tăng dần, rồi thứ hạng.
WITH total_paid AS (
	SELECT 
		EXTRACT(YEAR FROM i.issued_date) AS year,
		p.patient_id,
		p.full_name,
		SUM(i.total_amount) AS total_amount
	FROM invoice i
	JOIN medical_record mr ON mr.medical_record_id = i.medical_record_id 
	JOIN appointment a ON a.appointment_id = mr.appointment_id 
	JOIN patient p ON p.patient_id = a.patient_id 
	WHERE i.invoice_status = 'Paid'
	GROUP BY EXTRACT(YEAR FROM i.issued_date), p.patient_id 
),
ranked AS (
	SELECT 
		year,
		full_name,
		total_amount,
		RANK() OVER (PARTITION BY year ORDER BY total_amount DESC) AS rank
	FROM total_paid
)
SELECT * 
FROM ranked
WHERE rank <= 3
ORDER BY year, rank;
	