from sqlalchemy import text
from data_generator.database import engine
from data_generator.config import INSTRUCTIONS_RATE, MIN_PRESCRIPTIONS_PER_RECORD, MAX_PRESCRIPTIONS_PER_RECORD
from data_generator.logging_config import setup_logging
import random
import logging

logger = logging.getLogger(__name__)

PRESCRIPTION_INSTRUCTIONS = [
    "Uống sau ăn, tránh vận động mạnh",
    "Uống thuốc đúng giờ, không tự ý ngưng thuốc",
    "Uống nhiều nước trong thời gian dùng thuốc",
    "Tái khám nếu triệu chứng không giảm sau 3 ngày",
    "Tránh đồ ăn cay nóng khi đang dùng thuốc",
    "Không uống thuốc khi đói",
]

def get_records_without_prescription(connection):
    query = text("""
        SELECT medical_record_id, record_date
        FROM medical_record
        WHERE diagnosis <> 'Sức khỏe bình thường'
        AND medical_record_id NOT IN (SELECT medical_record_id FROM prescription) 
    """)
    return connection.execute(query).all()

def random_instructions():
    if random.random() < INSTRUCTIONS_RATE:
        return random.choice(PRESCRIPTION_INSTRUCTIONS)
    else:
        return None

def build_prescription_data(record):
    medical_record_id, record_date = record
    return {
        "medical_record_id": medical_record_id,
        "prescribed_date": record_date,
        "instructions": random_instructions()
    }

def seed_prescriptions():
    logger.info("Starting prescription seeding")

    with engine.begin() as connection:
        records = get_records_without_prescription(connection)
        if not records:
            logger.info("No records without prescriptions found.")
            return

        prescription_data = [
            build_prescription_data(record)
            for record in records
            for _ in range(random.randint(MIN_PRESCRIPTIONS_PER_RECORD, MAX_PRESCRIPTIONS_PER_RECORD))
        ]

        insert_query = text("""
            INSERT INTO prescription (
                medical_record_id,
                prescribed_date,
                instructions
            )
            VALUES (
            :medical_record_id,
            :prescribed_date,
            :instructions
            )
        """)

        connection.execute(insert_query, prescription_data)

    logger.info(f"Inserted {len(prescription_data)} prescription for completed medical record")
    logger.info("Prescriptions seeding completed")


if __name__ == "__main__":
    setup_logging()
    seed_prescriptions()