from sqlalchemy import text
import random
import logging
from data_generator.logging_config import setup_logging
from datetime import date, timedelta
from data_generator.database import engine
from data_generator.common import (
    random_gender,
    build_full_name,
    random_phone_number,
    random_date_between
)
from data_generator.config import NUM_DOCTORS 

logger = logging.getLogger(__name__)

CONSULTATION_FEES = [200000, 250000, 300000, 400000, 500000]

def get_departments(connection):
    query = text("SELECT department_id, department_name FROM department")
    return connection.execute(query).all()

def random_doctor_dates():
    date_of_birth = random_date_between(date(1960, 1, 1), date(1992, 12, 31))
    earliest_hire = date_of_birth + timedelta(days=25 * 365)
    hire_date = random_date_between(earliest_hire, date(2019, 12, 31))
    return date_of_birth, hire_date

def build_doctor_data(index, departments):
    department_id, department_name = random.choice(departments)
    gender = random_gender()
    full_name = f"BS. {build_full_name(gender)}"
    date_of_birth, hire_date = random_doctor_dates()
    return {
        "full_name": full_name,
        "gender": gender,
        "phone_number": random_phone_number(),
        "department_id": department_id,
        "specialty": department_name,
        "hire_date": hire_date,
        "date_of_birth": date_of_birth,
        "work_email": f"doctor{index:04d}@hospital.com",
        "license_number": f"BS-{hire_date.year}-{index:06d}",
        "consultation_fee": random.choice(CONSULTATION_FEES)
    }

def seed_doctors():
    logger.info("Starting doctors seeding")

    with engine.begin() as connection:
        count_query = text("SELECT COUNT(*) FROM doctor")
        current_count = connection.execute(count_query).scalar_one()

        missing_count = max(0, NUM_DOCTORS - current_count)

        departments = get_departments(connection)

        doctor_data = [
            build_doctor_data(index, departments)
            for index in range(current_count, current_count + missing_count)
        ]

        if doctor_data:
            insert_query = text("""
                INSERT INTO doctor (
                    full_name,
                    date_of_birth,
                    gender,
                    phone_number,
                    work_email, 
                    specialty,
                    consultation_fee,
                    department_id,
                    license_number,
                    hire_date
                )
                VALUES (
                    :full_name,
                    :date_of_birth,
                    :gender,
                    :phone_number,
                    :work_email,
                    :specialty,
                    :consultation_fee,
                    :department_id,
                    :license_number,
                    :hire_date
                )
            """)

            connection.execute(insert_query, doctor_data)

    logger.info(f"Doctors before insert : {current_count}")
    logger.info(f"Doctors insert : {len(doctor_data)}")
    logger.info(f"Target doctor : {NUM_DOCTORS}")
    logger.info("Doctors seeding completed")

if __name__ == "__main__":
    setup_logging()
    seed_doctors()