-- Migration : V049
-- Description : Add index to appointment table
-- Author : Xuan Hai
-- Date : 2026-08-16

CREATE INDEX idx_appointment_patient_id ON appointment (patient_id);
CREATE INDEX idx_appointment_doctor_id ON appointment (doctor_id);
CREATE INDEX idx_appointment_date ON appointment (appointment_date);