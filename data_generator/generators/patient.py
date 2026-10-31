import random
from datetime import date
from data_generator.config import EMERGENCY_CONTACT_RATE, NUM_PATIENTS
from data_generator.logging_config import setup_logging
from data_generator.database import engine
import logging
from sqlalchemy import text
from data_generator.common import (
    random_date_between,
    random_gender,
    random_phone_number,
    build_full_name
)

logger = logging.getLogger(__name__) 

STREET_NAMES = ["Nguyễn Trãi", "Lê Lợi", "Trần Hưng Đạo", "Phan Đình Phùng", "Nguyễn Thị Minh Khai", "Lý Thường Kiệt", "Nguyễn Văn Cừ", "Trần Phú", "Phạm Ngọc Thạch", "Nguyễn Du"]
CITIES = ["Hà Nội", "Hồ Chí Minh", "Đà Nẵng", "Hải Phòng", "Cần Thơ", "Nha Trang", "Huế", "Vũng Tàu", "Biên Hòa", "Buôn Ma Thuột"]

def random_birth_date():
    return random_date_between(date(1935, 1, 1), date(2019, 12, 31))

def random_address():
    house_number = random.randint(1, 200)
    street = random.choice(STREET_NAMES)
    city = random.choice(CITIES)
    return f"{house_number} {street}, {city}"

def random_emergency_contact():
    if random.random() < EMERGENCY_CONTACT_RATE:
        name = build_full_name(random_gender())
        phone = random_phone_number()
        return name, phone
    return None, None

def build_patient_data(index):
    gender = random_gender()
    full_name = build_full_name(gender)
    phone_number = random_phone_number()
    address = random_address()
    contact_name, contact_phone = random_emergency_contact()
    return {
        "full_name": full_name,
        "gender": gender,
        "date_of_birth": random_birth_date(),
        "phone_number": phone_number,
        "address": address,
        "identity_number": f"034{index:09d}",
        "emergency_contact_name": contact_name,
        "emergency_contact_phone": contact_phone
    }

def seed_patients():
    logger.info("Starting patient seeding")

    with engine.begin() as connection:
        count_query = text("SELECT COUNT(*) FROM patient")
        current_count = connection.execute(count_query).scalar_one()

        missing_count = max(0, NUM_PATIENTS  - current_count)

        patient_data = [
            build_patient_data(index)
            for index in range(current_count, current_count + missing_count)
        ]

        if patient_data:
            insert_query = text("""
                INSERT INTO patient (
                    full_name, 
                    date_of_birth,
                    gender,
                    phone_number,
                    address,
                    identity_number,
                    emergency_contact_name,
                    emergency_contact_phone
                    )
                VALUES (
                    :full_name, 
                    :date_of_birth,
                    :gender,
                    :phone_number,
                    :address,
                    :identity_number,
                    :emergency_contact_name,
                    :emergency_contact_phone
                )
            """)

            connection.execute(insert_query, patient_data)

    logger.info(f"Patients before insert : {current_count}")
    logger.info(f"Patients inserted : {len(patient_data)}")
    logger.info(f"Target patients : {NUM_PATIENTS}")
    logger.info("Patient seeding completed")

if __name__ == "__main__":
    setup_logging()
    seed_patients()