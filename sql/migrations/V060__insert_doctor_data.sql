-- Migration : V061
-- Description : Insert sample data into doctor table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO doctor (full_name, date_of_birth, gender, phone_number, work_email, specialty, consultation_fee, department_id, license_number, hire_date)
VALUES 
    ('BS. Nguyễn Minh Tuấn', '1975-04-15', 'Male', '0911111111', 'tuannm@hospital.com', 'Tim mạch', 300000.00, 1, 'BS-2010-001234', '2010-06-01'),
    ('BS. Trần Thị Hương', '1980-09-22', 'Female', '0922222222', 'huongtt@hospital.com', 'Nội tổng quát', 200000.00, 2, 'BS-2012-005678', '2012-03-15'),
    ('BS. Lê Văn Phong', '1983-02-10', 'Male', '0933333333', 'phonglv@hospital.com', 'Nhi khoa', 250000.00, 3, 'BS-2015-009876', '2015-09-01'),
    ('BS. Phạm Thị Mai', '1978-12-05', 'Female', '0944444444', 'maipt@hospital.com', 'Ngoại khoa', 400000.00, 4, 'BS-2011-003456', '2011-01-20'),
    ('BS. Hoàng Văn Đức', '1988-06-18', 'Male', '0955555555', 'ducvh@hospital.com', 'Tim mạch', 280000.00, 1, 'BS-2018-007890', '2018-07-10');