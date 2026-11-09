from data_generator.config import (
    DIRTY_PHONE_RATE, NUM_PATIENTS,
    DIRTY_APPOINTMENT_TIME_RATE, NUM_APPOINTMENTS,
    DIRTY_RECORD_DATE_RATE
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

def dirty_appointment_times(connection):
    dirty_count = int(NUM_APPOINTMENTS * DIRTY_APPOINTMENT_TIME_RATE)

    result = connection.execute(
        text("""
            UPDATE appointment 
            SET appointment_time = '02:30'
            WHERE appointment_id IN (
                SELECT appointment_id FROM appointment ORDER BY RANDOM() LIMIT :limit
            )
        """),
        {"limit": dirty_count}
    )

    return result.rowcount

def dirty_record_dates(connection):
    total = connection.execute(text("SELECT COUNT(*) FROM medical_record")).scalar_one()
    dirty_count = int(total * DIRTY_RECORD_DATE_RATE)

    result = connection.execute(
        text("""
            UPDATE medical_record
            SET record_date = record_date - 3
            WHERE medical_record_id IN (
                SELECT medical_record_id FROM medical_record ORDER BY RANDOM() LIMIT :limit
            )
        """),
        {"limit": dirty_count}
    )

    return result.rowcount

if __name__ == "__main__":
    setup_logging()
    with engine.begin() as connection:
        #changed = dirty_phone_numbers(connection)
        #changed = dirty_appointment_times(connection)
        changed = dirty_record_dates(connection)
    logger.info("Corrupted %s medical record dates", changed)