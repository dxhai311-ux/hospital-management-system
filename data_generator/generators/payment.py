from data_generator.database import engine
from sqlalchemy import text
import random
from data_generator.logging_config import setup_logging
import logging

logger = logging.getLogger(__name__)

PAYMENT_METHODS = ["Cash", "Credit Card", "Bank Transfer"]

def get_paid_invoices_without_payment(connection):
    query = text("""
        SELECT invoice_id, total_amount, issued_date
        FROM invoice
        WHERE invoice_status = 'Paid'
        AND invoice_id NOT IN (SELECT invoice_id FROM payment)
    """)
    return connection.execute(query).all()

def random_payment_method():
    return random.choice(PAYMENT_METHODS)

def build_transaction_reference(invoice_id, method):
    if method == "Cash":
        return None
    else:
        return f"TXN{invoice_id:09d}"

def build_payment_data(invoice):
    invoice_id, total_amount, issued_date = invoice
    method = random_payment_method()
    return {
        "invoice_id": invoice_id,
        "payment_method": method,
        "payment_date": issued_date,
        "payment_amount": total_amount,
        "payment_status": "Successful",
        "transaction_reference": build_transaction_reference(invoice_id, method)
    }

def seed_payments():
    logger.info("Starting payment seeding")

    with engine.begin() as connection:
        invoices = get_paid_invoices_without_payment(connection)
        if not invoices:
            logger.info("No paid invoices without payments found")
            return

        payment_data = [
            build_payment_data(invoice)
            for invoice in invoices
        ]

        insert_query = text("""
            INSERT INTO payment (
                invoice_id,
                payment_method,
                payment_date,
                payment_amount,
                payment_status,
                transaction_reference
            ) VALUES (
                :invoice_id,
                :payment_method,
                :payment_date,
                :payment_amount,
                :payment_status,
                :transaction_reference
            )
        """)
        connection.execute(insert_query, payment_data)

    logger.info(f"Inserted {len(payment_data)} payments for paid invoices")
    logger.info("Payments seeding completed")

if __name__ == "__main__":
    setup_logging()
    seed_payments()