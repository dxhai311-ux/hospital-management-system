from data_generator.database import engine
import pandas as pd

def extract_appointment():
    df = pd.read_sql("""
        SELECT  a.appointment_id,
                a.patient_id, 
                a.doctor_id,
                d.department_id,
                a.appointment_date,
                a.appointment_time,
                a.appointment_status,
                a.room_id
        FROM appointment a 
        JOIN doctor d ON a.doctor_id = d.doctor_id
    """, engine)
    return df

if __name__ == "__main__":
    df = extract_appointment()
    print(df.shape)
    print(df.head())