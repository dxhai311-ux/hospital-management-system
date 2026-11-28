INSERT INTO dw.dim_doctor (
    doctor_id,
    full_name,
	gender,
	specialty,
	employment_status
)
SELECT 
	doctor_id,
 	full_name,
    gender,
	specialty,
    employment_status
FROM public.doctor
ON CONFLICT (doctor_id)
DO UPDATE SET 
    full_name = EXCLUDED.full_name,
    gender = EXCLUDED.gender,
    specialty = EXCLUDED.specialty,
    employment_status = EXCLUDED.employment_status;