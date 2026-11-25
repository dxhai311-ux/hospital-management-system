from etl.extract import extract_appointment

def transform_appointment(df):
    df = df.copy()
    df["appointment_status"] = df["appointment_status"].replace(["Complete", "completed"], "Completed")
    return df

if __name__ == "__main__":
    df = extract_appointment()
    clean_df = transform_appointment(df)
    print(clean_df['appointment_status'].value_counts())