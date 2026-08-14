-- Migration : V006
-- Description : Create Appointment Table
-- Author : Xuan Hai
-- Date : 2026-08-14

CREATE TABLE appointment (
    appointment_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    patient_id INT REFERENCES patient(patient_id),
    doctor_id INT REFERENCES doctor(doctor_id),
    appointment_date DATE,
    appointment_time TIME,
    room_id INT REFERENCES room(room_id),
    reason TEXT,
    appointment_status VARCHAR(20)
)