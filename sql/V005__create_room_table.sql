-- Migration : V005
-- Description : Create Room Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE room (
    room_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room_name VARCHAR(50),
    room_type VARCHAR(50),
    department_id INT REFERENCES department(department_id),
    capacity INT,
    location VARCHAR(100),
    room_status VARCHAR(20)
)