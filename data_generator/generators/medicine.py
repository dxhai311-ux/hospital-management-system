import random
from datetime import date, timedelta
from data_generator.config import NUM_MEDICINES
from data_generator.logging_config import setup_logging
from data_generator.database import engine
import logging
from sqlalchemy import text
from data_generator.common import random_date_between

logger = logging.getLogger(__name__)

MEDICINES = [
    #(name, active_ingredient, unit, strength, unit_price)
    ("Paracetamol", "Paracetamol", "Tablet", "650mg", 2500),
    ("Paracetamol", "Paracetamol", "Syrup", "120mg/5ml", 12000),
    ("Ibuprofen", "Ibuprofen", "Tablet", "200mg", 3000),
    ("Diclofenac", "Diclofenac sodium", "Tablet", "50mg", 1500),
    ("Meloxicam", "Meloxicam", "Tablet", "7.5mg", 2000),
    ("Amoxicillin", "Amoxicillin", "Capsule", "500mg", 6000),
    ("Amoxicillin/Clavulanate", "Amoxicillin + Clavulanic acid", "Tablet", "625mg", 15000),
    ("Cefuroxime", "Cefuroxime axetil", "Tablet", "500mg", 18000),
    ("Cefixime", "Cefixime", "Capsule", "200mg", 12000),
    ("Azithromycin", "Azithromycin", "Tablet", "500mg", 25000),
    ("Ciprofloxacin", "Ciprofloxacin", "Tablet", "500mg", 4000),
    ("Metronidazole", "Metronidazole", "Tablet", "250mg", 1000),
    ("Doxycycline", "Doxycycline", "Capsule", "100mg", 2500),
    ("Omeprazole", "Omeprazole", "Capsule", "20mg", 3500),
    ("Esomeprazole", "Esomeprazole", "Tablet", "40mg", 9000),
    ("Domperidone", "Domperidone", "Tablet", "10mg", 1500),
    ("Loperamide", "Loperamide hydrochloride", "Capsule", "2mg", 1200),
    ("Ambroxol", "Ambroxol hydrochloride", "Tablet", "30mg", 1500),
    ("Metformin", "Metformin hydrochloride", "Tablet", "500mg", 1200),
    ("Gliclazide", "Gliclazide", "Tablet", "80mg", 2500),
    ("Amlodipine", "Amlodipine besylate", "Tablet", "5mg", 1500),
    ("Losartan", "Losartan potassium", "Tablet", "50mg", 3000),
    ("Enalapril", "Enalapril maleate", "Tablet", "10mg", 1800),
    ("Atorvastatin", "Atorvastatin calcium", "Tablet", "20mg", 4500),
    ("Simvastatin", "Simvastatin", "Tablet", "20mg", 3000),
    ("Aspirin", "Acetylsalicylic acid", "Tablet", "81mg", 1000),
    ("Clopidogrel", "Clopidogrel", "Tablet", "75mg", 7000),
    ("Furosemide", "Furosemide", "Tablet", "40mg", 800),
    ("Bisoprolol", "Bisoprolol fumarate", "Tablet", "5mg", 4000),
    ("Salbutamol", "Salbutamol", "Inhaler", "100mcg", 65000),
    ("Montelukast", "Montelukast sodium", "Tablet", "10mg", 9000),
    ("Cetirizine", "Cetirizine hydrochloride", "Tablet", "10mg", 1500),
    ("Loratadine", "Loratadine", "Tablet", "10mg", 1800),
    ("Prednisolone", "Prednisolone", "Tablet", "5mg", 700),
    ("Methylprednisolone", "Methylprednisolone", "Tablet", "16mg", 4000),
    ("Acetylcysteine", "Acetylcysteine", "Sachet", "200mg", 3500),
    ("Vitamin B1", "Thiamine", "Tablet", "100mg", 600),
    ("Vitamin D3", "Cholecalciferol", "Drops", "400IU", 40000),
    ("Calcium", "Calcium carbonate", "Tablet", "500mg", 1500),
    ("Folic acid", "Folic acid", "Tablet", "5mg", 500),
]

MANUFACTURERS = ["Traphaco", "DHG Pharma", "Imexpharm", "Domesco", "Stada Vietnam"]

ALL_PRODUCTS = [
    (medicine, manufacturer)
    for medicine in MEDICINES
    for manufacturer in MANUFACTURERS
]

def random_manufacture_and_expiry():
    manufacture_date = random_date_between(date(2025, 1, 1), date(2026, 10, 29))
    shelf_life_days = random.randint(540, 1095)
    expiry_date = manufacture_date + timedelta(days=shelf_life_days)
    return manufacture_date, expiry_date

def build_medicine_data(index):
    medicine, manufacturer = ALL_PRODUCTS[index]
    name, ingredient, unit, strength, unit_price = medicine
    manufacture_date, expiry_date = random_manufacture_and_expiry()
    return {
        "medicine_name": name,
        "active_ingredient": ingredient,
        "unit": unit,
        "strength": strength,
        "unit_price": unit_price,
        "manufacturer": manufacturer,
        "manufacture_date": manufacture_date,
        "expiry_date": expiry_date,
        "stock_quantity": random.randint(50, 1000)
    }

def seed_medicines():
    logger.info("Starting medicine seeding")

    with engine.begin() as connection:
        count_query = text("SELECT COUNT(*) FROM medicine")
        current_count = connection.execute(count_query).scalar_one()

        missing_count = max(0, NUM_MEDICINES - current_count)

        medicine_data = [
            build_medicine_data(index)
            for index in range(current_count, current_count + missing_count)
        ]

        if medicine_data:
            insert_query = text("""
                INSERT INTO medicine (
                    medicine_name,
                    active_ingredient,
                    unit,
                    strength,
                    manufacturer,
                    manufacture_date,
                    expiry_date,
                    stock_quantity,
                    unit_price
                )
                VALUES (
                    :medicine_name,
                    :active_ingredient,
                    :unit,
                    :strength,
                    :manufacturer,
                    :manufacture_date,
                    :expiry_date,
                    :stock_quantity,
                    :unit_price
                )
            """)

            connection.execute(insert_query, medicine_data)
    logger.info(f"Medicines before insert : {current_count}")
    logger.info(f"Medicines inserted : {len(medicine_data)}")
    logger.info(f"Target medicines : {NUM_MEDICINES}")
    logger.info("Medicine seeding completed")


if __name__ == "__main__":
    setup_logging()
    seed_medicines()
