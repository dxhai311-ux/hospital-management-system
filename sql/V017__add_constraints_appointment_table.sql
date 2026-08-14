-- Migration : V017
-- Description : Add Constraints to Appointment Table
-- Author : Xuan Hai
-- Date : 2026-08-14

ALTER TABLE appointment
    ALTER COLUMN patient_id SET NOT NULL,
    ALTER COLUMN doctor_id SET NOT NULL,
    ALTER COLUMN appointment_date SET NOT NULL,
    ALTER COLUMN appointment_time SET NOT NULL,
    ALTER COLUMN room_id SET NOT NULL,
    ALTER COLUMN appointment_status SET NOT NULL;