-- Migration : V058
-- Description : Insert sample data into department table
-- Author : Xuan Hai
-- Date : 2026-08-19

INSERT INTO department (department_name, description, location, phone_number)
VALUES 
    ('Tim mạch', 'Chuyên khoa điều trị các bệnh về tim và mạch máu', 'Tầng 2, Tòa A', '0243123456'),
    ('Nội tổng quát', 'Khám và điều trị các bệnh nội khoa thông thường', 'Tầng 1, Tòa A', '0243123457'),
    ('Nhi khoa', 'Chuyên khoa dành cho trẻ em', 'Tầng 3, Tòa B', '0243123458'),
    ('Ngoại khoa', 'Chuyên khoa phẫu thuật', 'Tầng 4, Tòa B', '0243123459');