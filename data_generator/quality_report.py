import pandas as pd
from data_generator.database import engine
import datetime

def read_table(table):
    return pd.read_sql(f"SELECT * FROM {table}", engine)

def print_result(label, count):
    return print(f"{label} : {count}")

def count_bad_phones():
    df = read_table('patient')
    is_invalid_phone = df['phone_number'].str.len() != 10
    return is_invalid_phone.sum()

def count_bad_appointment_times():
    df = read_table('appointment')
    too_early = df['appointment_time'] < datetime.time(8, 0)
    too_late = df['appointment_time'] > datetime.time(16, 30)
    return (too_early | too_late).sum()

def count_bad_appointment_statuses():
    df = read_table('appointment')
    is_invalid_status = ~df['appointment_status'].isin(['Completed', 'No Show', 'Scheduled', 'Cancelled']) 
    return is_invalid_status.sum()

def count_bad_record_dates():
    df_a = read_table('appointment')
    df_mr = read_table('medical_record')
    merged = pd.merge(df_a, df_mr, on='appointment_id', how='inner')
    is_date_mismatch = merged['appointment_date'] != merged['record_date']
    return is_date_mismatch.sum()

def count_bad_payment_dates():
    df_i = read_table('invoice')
    df_p = read_table('payment')
    merged = pd.merge(df_i, df_p, on='invoice_id', how='inner')
    is_date_mismatch = merged['issued_date'] != merged['payment_date']
    return is_date_mismatch.sum()

def count_duplicate_patients():
    df = read_table('patient')
    is_duplicate = df.duplicated(subset=['full_name', 'phone_number', 'date_of_birth', 'address'], keep='first')
    return is_duplicate.sum()

if __name__ == "__main__":
    print_result('Invalid phone numbers', count_bad_phones())
    print_result('Appointment times outside working hours', count_bad_appointment_times())
    print_result('Invalid appointment statuses', count_bad_appointment_statuses())
    print_result('Medical record dates not matching appointment date', count_bad_record_dates())
    print_result('Payment dates not matching invoice date', count_bad_payment_dates())
    print_result('Duplicate patients', count_duplicate_patients())