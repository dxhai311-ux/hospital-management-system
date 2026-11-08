from sqlalchemy import text
from data_generator.database import engine
import random
from data_generator.logging_config import setup_logging
import logging
from data_generator.config import MIN_MEDICINES_PER_PRESCRIPTION, MAX_MEDICINES_PER_PRESCRIPTION
logger = logging.getLogger(__name__)

DOSAGES = [("1 viên", 1), ("2 viên", 2)]
FREQUENCIES = [("1 lần/ngày", 1), ("2 lần/ngày", 2), ("3 lần/ngày", 3)]
DURATIONS = [("3 ngày", 3), ("5 ngày", 5), ("7 ngày", 7), ("10 ngày", 10), ("14 ngày", 14)]

def get_prescriptions_without_items(connection):
    query = text("""
        SELECT prescription_id 
        FROM prescription
        WHERE prescription_id NOT IN (SELECT prescription_id FROM prescription_item)
    """)
    return connection.execute(query).scalars().all()

def get_medicine_ids(connection):
    query = text("SELECT medicine_id FROM medicine")
    return connection.execute(query).scalars().all()

def random_dosage_info():
    dosage, pills = random.choice(DOSAGES)
    frequency, times = random.choice(FREQUENCIES)
    duration, days = random.choice(DURATIONS)
    quantity = pills * times * days
    return dosage, frequency, duration, quantity

def build_prescription_item_data(prescription_id, medicine_id):
    dosage, frequency, duration, quantity = random_dosage_info()
    return {
        "prescription_id": prescription_id,
        "medicine_id": medicine_id,
        "quantity": quantity,
        "dosage": dosage,
        "frequency": frequency,
        "duration": duration
    }

def seed_prescription_items():
    logger.info("Starting prescription item seeding")

    with engine.begin() as connection:
        prescription_ids = get_prescriptions_without_items(connection)
        if not prescription_ids:
            logger.info("No prescriptions without items found")
            return 

        medicine_ids = get_medicine_ids(connection)

        item_data = [
            build_prescription_item_data(prescription_id, medicine_id)
            for prescription_id in prescription_ids
            for medicine_id in random.sample(medicine_ids, random.randint(MIN_MEDICINES_PER_PRESCRIPTION, MAX_MEDICINES_PER_PRESCRIPTION))
        ]

        insert_query = text("""
            INSERT INTO prescription_item (
                prescription_id,
                medicine_id, 
                dosage,
                duration,
                frequency,
                quantity
            ) VALUES (
                :prescription_id, 
                :medicine_id, 
                :dosage,
                :duration,
                :frequency,
                :quantity
            )
        """)
        connection.execute(insert_query, item_data)

    logger.info(f"Inserted {len(item_data)} prescription items for {len(prescription_ids)} prescriptions")
    logger.info("Prescription items seeding completed")

if __name__ == "__main__":
    setup_logging()
    seed_prescription_items()