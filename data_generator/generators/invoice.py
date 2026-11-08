from sqlalchemy import text
from data_generator.database import engine
from data_generator.config import PAYMENT_RATE
import random
from data_generator.logging_config import setup_logging
import logging

logger = logging.getLogger(__name__)

def get_records_with_totals(connection):
    query = text("""
        SELECT 
            mr.medical_record_id,
            mr.record_date,
            d.consultation_fee + COALESCE(SUM(pi.quantity * m.unit_price), 0) AS total_amount
        FROM medical_record mr
        JOIN appointment a ON mr.appointment_id = a.appointment_id
        JOIN doctor d ON a.doctor_id = d.doctor_id
        LEFT JOIN prescription p ON mr.medical_record_id  = p.medical_record_id 
        LEFT JOIN prescription_item pi ON p.prescription_id  = pi.prescription_id 
        LEFT JOIN medicine m ON m.medicine_id  = pi.medicine_id 
        WHERE mr.medical_record_id NOT IN (SELECT medical_record_id FROM invoice)
        GROUP BY mr.medical_record_id, mr.record_date, d.consultation_fee
    """)
    return connection.execute(query).all()

def random_invoice_status():
    if random.random() < PAYMENT_RATE:
        return "Paid"
    else:
        return "Unpaid"

def build_invoice_data(record):
    medical_record_id, record_date, total_amount = record
    return {
        "medical_record_id": medical_record_id,
        "total_amount": total_amount,
        "issued_date": record_date,
        "invoice_status": random_invoice_status()
    }

def seed_invoices():
    logger.info("Starting invoice seeding")

    with engine.begin() as connection:
        records = get_records_with_totals(connection)
        if not records:
            logger.info("No medical records without invoices found")
            return

        invoice_data = [
            build_invoice_data(record)
            for record in records
        ]

        insert_query = text("""
            INSERT INTO invoice (
                medical_record_id,
                total_amount,
                issued_date,
                invoice_status
            ) VALUES (
                :medical_record_id,
                :total_amount,
                :issued_date,
                :invoice_status
            )
        """)
        connection.execute(insert_query, invoice_data)

    logger.info(f"Inserted {len(invoice_data)} invoices")
    logger.info("Invoices seeding completed")

if __name__ == "__main__":
    setup_logging()
    seed_invoices()