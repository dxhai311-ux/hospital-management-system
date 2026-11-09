from data_generator.config import (
    DIRTY_PHONE_RATE,
    NUM_PATIENTS
)
from sqlalchemy import text
from data_generator.logging_config import setup_logging
import logging
from data_generator.database import engine

logger = logging.getLogger(__name__)

def dirty_phone_numbers(connection):
    dirty_count = int(NUM_PATIENTS * DIRTY_PHONE_RATE)

    result = connection.execute(
        text("""
            UPDATE patient
            SET phone_number = SUBSTRING(phone_number FROM 2)
            WHERE patient_id IN (
                SELECT patient_id FROM patient ORDER BY RANDOM() LIMIT :limit
            )
        """),
        {"limit": dirty_count}
    )

    return result.rowcount

if __name__ == "__main__":
    setup_logging()
    with engine.begin() as connection:
        changed = dirty_phone_numbers(connection)
    logger.info("Update %s dirty phone number patient", changed)