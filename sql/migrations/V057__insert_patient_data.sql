-- Migration : V058
-- Description : Insert sample data into patient table
-- Author : Xuan Hai
-- Date : 2026-08-17

INSERT INTO patient (full_name, date_of_birth, gender, phone_number, address, identity_number, emergency_contact_name, emergency_contact_phone)
VALUES 
    ('Nguyễn Văn An', '1985-03-12', 'Male', '0901234567', '12 Trần Hưng Đạo, Hà Nội', '001085001234', 'Nguyễn Thị Lan', '0909876543'),
    ('Trần Thị Bình', '1992-07-25', 'Female', '0912345678', '45 Lê Lợi, Đà Nẵng', '001092005678', NULL, NULL),
    ('Lê Văn Cường', '1978-11-03', 'Male', '0923456789', '78 Nguyễn Huệ, TP.HCM', NULL, 'Lê Thị Hoa', '0987654321'),
    ('Phạm Thị Dung', '2000-01-18', 'Female', '0934567890', '23 Hai Bà Trưng, Hải Phòng', '001100009876', 'Phạm Văn Sơn', '0976543210'),
    ('Hoàng Văn Em', '1995-09-30', 'Male', '0945678901', '56 Trường Chinh, Cần Thơ', NULL, NULL, NULL);