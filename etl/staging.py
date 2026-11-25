from etl.transform import transform_appointment
from etl.extract import extract_appointment
from data_generator.database import engine

def write_to_staging(df):
    return df.to_sql("appointment", engine, schema="staging", if_exists="replace", index=False)

if __name__ == "__main__":
    df = extract_appointment()
    clean_df = transform_appointment(df)
    write_to_staging(clean_df)