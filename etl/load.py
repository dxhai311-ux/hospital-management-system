from data_generator.database import engine
from sqlalchemy import text

LOAD_DIM_DEPARTMENT = """
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
"""

def load_dim_department():
    with engine.begin() as connection:
        connection.execute(text(LOAD_DIM_DEPARTMENT))

if __name__ == "__main__":
    load_dim_department()