-- Migration : V047
-- Description : Add index to doctor table
-- Author : Xuan Hai
-- Date : 2026-08-16

CREATE INDEX idx_doctor_specialty ON doctor (specialty);
CREATE INDEX idx_doctor_department_id ON doctor (department_id);