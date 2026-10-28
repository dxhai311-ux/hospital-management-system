from sqlalchemy import text 

from data_generator.config import NUM_DEPARTMENTS
from data_generator.database import engine
from data_generator.logging_config import setup_logging
import logging

logger = logging.getLogger(__name__)

DEPARTMENT_NAMES = [
    # 1–10
    "Da liễu",
    "Thần kinh",
    "Nội tiết",
    "Hô hấp",
    "Tiêu hóa",
    "Tai Mũi Họng",
    "Mắt",
    "Răng Hàm Mặt",
    "Ung bướu",
    "Chấn thương chỉnh hình",

    # 11–20
    "Thận - Tiết niệu",
    "Sản khoa",
    "Phụ khoa",
    "Hỗ trợ sinh sản",
    "Hồi sức cấp cứu",
    "Gây mê hồi sức",
    "Chẩn đoán hình ảnh",
    "Xét nghiệm",
    "Giải phẫu bệnh",
    "Truyền nhiễm",

    # 21–30
    "Y học cổ truyền",
    "Phục hồi chức năng",
    "Vật lý trị liệu",
    "Dinh dưỡng",
    "Tâm thần",
    "Tâm lý lâm sàng",
    "Lão khoa",
    "Huyết học",
    "Miễn dịch",
    "Dị ứng",

    # 31–40
    "Di truyền y học",
    "Ngoại thần kinh",
    "Ngoại lồng ngực",
    "Ngoại tim mạch",
    "Ngoại tiêu hóa",
    "Ngoại tiết niệu",
    "Ngoại nhi",
    "Phẫu thuật tạo hình",
    "Bỏng",
    "Nội tim mạch",

    # 41–51
    "Nội thận",
    "Nội cơ xương khớp",
    "Nội gan mật",
    "Nội lão",
    "Nhi sơ sinh",
    "Nhi tim mạch",
    "Nhi hô hấp",
    "Nhi tiêu hóa",
    "Nhi thần kinh",
    "Y học thể thao",
    "Kiểm soát nhiễm khuẩn",
]

DEPARTMENT_LOCATIONS = [
    "Tầng 1, Tòa A",
    "Tầng 2, Tòa A",
    "Tầng 3, Tòa A",
    "Tầng 1, Tòa B",
    "Tầng 2, Tòa B",
    "Tầng 3, Tòa B",
    "Tầng 1, Tòa C",
    "Tầng 2, Tòa C",
    "Tầng 3, Tòa C",
    "Tầng 4, Tòa C",
]

def build_department_data(department_name, index):
    location_index = index % len(DEPARTMENT_LOCATIONS)
    location = DEPARTMENT_LOCATIONS[location_index]

    phone_number = f"0173{300000 + index:06d}"

    return {
        "department_name": department_name,
        "description": f"Chuyên khoa {department_name} tại bệnh viện",
        "location": location,
        "phone_number": phone_number,
    }

def seed_departments():
    logger.info("Starting department seeding")

    with engine.begin() as connection:
        count_query = text("SELECT COUNT(*) FROM department")
        current_count = connection.execute(count_query).scalar_one()

        names_query = text("SELECT department_name FROM department")
        existing_names = set(
            connection.execute(names_query).scalars().all()
        )

        #max(0,...) để tránh dữ liệu bị
        missing_count = max(0, NUM_DEPARTMENTS - current_count) 

        new_names = [
            name 
            for name in DEPARTMENT_NAMES
            if name not in existing_names
        ]

        names_to_insert = new_names[:missing_count]

        department_data = [
            build_department_data(name, index)
            for index, name in enumerate(names_to_insert)
        ]

        if department_data:
            insert_query = text("""
                INSERT INTO department (
                    department_name,
                    description,
                    location,
                    phone_number
                )
                VALUES (
                    :department_name,
                    :description,
                    :location,
                    :phone_number
                )
            """)

            connection.execute(insert_query, department_data)

    logger.info(f"Departments before insert : {current_count}")
    logger.info(f"Departments inserted : {len(department_data)}")
    logger.info(f"Target departments : {NUM_DEPARTMENTS}")
    logger.info("Department seeding completed")

if __name__ == "__main__":
    setup_logging()
    seed_departments()
