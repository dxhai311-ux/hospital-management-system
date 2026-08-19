-- Migration : V064
-- Description : Insert sample data into medical_record table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO medical_record (appointment_id, diagnosis, symptoms, treatment, notes, record_date)
VALUES 
    (1, 'Thiếu máu cơ tim', 'Đau ngực, khó thở khi gắng sức', 'Kê thuốc giãn mạch, hẹn tái khám sau 2 tuần', 'Bệnh nhân cần theo dõi huyết áp thường xuyên', '2026-08-20'),
    (3, 'Viêm họng cấp', 'Sốt 38.5°C, đau họng, ho khan', 'Kê kháng sinh và thuốc hạ sốt', NULL, '2026-08-21'),
    (4, 'Sức khỏe bình thường', 'Không có triệu chứng bất thường', 'Không cần điều trị, tái khám định kỳ 6 tháng', NULL, '2026-08-22');