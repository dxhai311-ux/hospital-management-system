from sqlalchemy import text
from data_generator.database import engine
import random
from data_generator.logging_config import setup_logging
from data_generator.config import NUM_ROOMS
import logging

logger = logging.getLogger(__name__)

ROOM_TYPES = [
    # (room_type, min_capacity, max_capacity)
    ("Consultation Room", 2, 3),
    ("Examination Room", 3, 5)
]

def get_rooms_per_department(connection):
    query = text("""
        SELECT department_id, COUNT(*)
        FROM room 
        GROUP BY department_id
    """)
    rows = connection.execute(query).all()
    return dict(rows)

def get_department_with_doctor(connection):
    query = text("""
        SELECT department_id, location
        FROM department
        WHERE department_id IN (SELECT DISTINCT department_id FROM doctor)
    """)
    return connection.execute(query).all()

def random_room_type_and_capacity():
    room_type, min_capacity, max_capacity = random.choice(ROOM_TYPES)
    capacity = random.randint(min_capacity, max_capacity)
    return room_type, capacity 

def build_room_data(index, departments, room_per_department):
    department_id, location = departments[index % len(departments)]
    count = room_per_department.get(department_id, 0)
    room_name = str(101 + count)
    room_per_department[department_id] = count + 1
    room_type, capacity = random_room_type_and_capacity()
    return {
        "room_name": room_name, 
        "room_type": room_type,
        "capacity": capacity,
        "department_id": department_id,
        "location": location
    }

def seed_rooms():
    logger.info("Starting room seeding")

    with engine.begin() as connection:
        count_query = text("SELECT COUNT(*) FROM room")
        current_count = connection.execute(count_query).scalar_one()

        missing_count = max(0, NUM_ROOMS - current_count)

        departments = get_department_with_doctor(connection)
        room_per_department = get_rooms_per_department(connection)

        room_data = [
            build_room_data(index, departments, room_per_department)
            for index in range(current_count, current_count + missing_count)
        ]

        if room_data:
            insert_query = text("""
                INSERT INTO room (
                    room_name, 
                    room_type,
                    capacity,
                    department_id,
                    location
                )
                VALUES (
                    :room_name, 
                    :room_type,
                    :capacity,
                    :department_id,
                    :location
                )
            """)

            connection.execute(insert_query, room_data)

    logger.info(f"Rooms before insert : {current_count}")
    logger.info(f"Rooms inserted : {len(room_data)}")
    logger.info(f"Target rooms : {NUM_ROOMS}")
    logger.info("Room seeding completed")
        


if __name__ == "__main__":
    setup_logging()
    seed_rooms()