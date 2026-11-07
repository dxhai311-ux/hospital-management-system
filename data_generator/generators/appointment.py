from sqlalchemy import text 
from data_generator.database import engine
from data_generator.logging_config import setup_logging
import logging
from data_generator.config import (
    FUTURE_APPOINTMENT_MONTHS,
    DATA_START_DATE,
    COMPLETED_RATE,
    CANCELLED_RATE,
    NO_SHOW_RATE,
    REASON_RATE,
    NUM_APPOINTMENTS
)
from datetime import date, timedelta, time
from data_generator.common import random_date_between
import random

logger = logging.getLogger(__name__)

APPOINTMENT_REASONS = [
    "Khám sức khỏe định kỳ",
    "Tái khám theo hẹn",
    "Đau đầu kéo dài",
    "Sốt kéo dài",
    "Ho kéo dài",
    "Đau bụng",
    "Mệt mỏi, chóng mặt",
    "Đau lưng, đau khớp",
    "Khám theo yêu cầu",
    "Tư vấn kết quả xét nghiệm",
]

def get_rooms_by_department(connection):
    query = text("""
        SELECT department_id, room_id
        FROM room 
        WHERE room_type IN ('Consultation Room', 'Examination Room')
    """)
    rows = connection.execute(query).all()
    rooms_per_department = {}
    for department_id, room_id in rows:
        if department_id not in rooms_per_department:
            rooms_per_department[department_id] = []
        rooms_per_department[department_id].append(room_id)

    return rooms_per_department

def get_doctors(connection):
    query = text("""
        SELECT doctor_id, department_id
        FROM doctor
    """)
    return connection.execute(query).all()

def get_patients_ids(connection):
    query = text("""
        SELECT patient_id
        FROM patient
    """)
    return connection.execute(query).scalars().all()

def random_appointment_date():
    start = date.fromisoformat(DATA_START_DATE)
    end = date.today() + timedelta(days=FUTURE_APPOINTMENT_MONTHS * 30)
    return random_date_between(start, end)

def random_appointment_time():
    hour = random.randint(8, 16)
    minute = random.choice([0, 15, 30])
    return time(hour, minute)

def random_appointment_status(appointment_date):
    if appointment_date >= date.today():
        return "Scheduled"
    else:
        return random.choices(
            ["Completed", "Cancelled", "No Show"],
            weights=[COMPLETED_RATE, CANCELLED_RATE, NO_SHOW_RATE],
            k=1 #tra ve 1 phan tu  
        )[0]
        
def random_reason():
    if random.random() < REASON_RATE:
        return random.choice(APPOINTMENT_REASONS)
    else:
        return None

def build_appointment_data(patient_ids, doctors, rooms_by_department):
    patient_id = random.choice(patient_ids)
    doctor_id, department_id = random.choice(doctors)
    room_id = random.choice(rooms_by_department[department_id])
    appointment_date = random_appointment_date()
    return {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "room_id": room_id,
        "appointment_date": appointment_date,
        "appointment_time": random_appointment_time(),
        "reason": random_reason(),
        "appointment_status": random_appointment_status(appointment_date)
    }

def seed_appointments():
    logger.info("Starting appointments seeding")

    with engine.begin() as connection:
        count_query = text("SELECT COUNT(*) FROM appointment")
        current_count = connection.execute(count_query).scalar_one()

        missing_count = max(0, NUM_APPOINTMENTS - current_count)

        patient_ids = get_patients_ids(connection)
        doctors = get_doctors(connection)
        rooms_by_department = get_rooms_by_department(connection)

        appointment_data = [
            build_appointment_data(patient_ids, doctors, rooms_by_department)
            for _ in range(missing_count)
        ]

        if appointment_data:
            insert_query = text("""
                INSERT INTO appointment (
                    patient_id,
                    doctor_id,
                    room_id,
                    appointment_date,
                    appointment_time,
                    reason,
                    appointment_status
                )
                VALUES (
                    :patient_id,
                    :doctor_id,
                    :room_id,
                    :appointment_date,
                    :appointment_time,
                    :reason,
                    :appointment_status
                )
            """)

            connection.execute(insert_query, appointment_data)

    logger.info(f"Appointments before insert : {current_count}")
    logger.info(f"Appointments inserted : {len(appointment_data)}")
    logger.info(f"Target appointments : {NUM_APPOINTMENTS}")
    logger.info(f"Appointment seeding completed")

if __name__ == "__main__":
    setup_logging()
    seed_appointments()
