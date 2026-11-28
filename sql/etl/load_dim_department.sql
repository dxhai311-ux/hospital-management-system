INSERT INTO dw.dim_department (
    department_id,
    department_name,
    location,
    department_status
)
SELECT 
    department_id,
    department_name,
    location,
    department_status
FROM public.department
ON CONFLICT (department_id)
DO UPDATE SET 
    department_name = EXCLUDED.department_name,
    location = EXCLUDED.location,
    department_status = EXCLUDED.department_status;