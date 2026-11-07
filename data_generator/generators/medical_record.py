from data_generator.database import engine
from sqlalchemy import text
import random
from data_generator.config import NOTES_RATE
from data_generator.logging_config import setup_logging
import logging

logger = logging.getLogger(__name__)

DISEASES_BY_REASON = {
    "Đau đầu kéo dài": [
        ("Đau đầu căng thẳng", "Đau âm ỉ hai bên đầu, căng cơ cổ vai", "Thuốc giảm đau, nghỉ ngơi, giảm căng thẳng"),
        ("Migraine", "Đau nửa đầu từng cơn, sợ ánh sáng, buồn nôn", "Thuốc cắt cơn đau, tránh yếu tố khởi phát"),
    ],
    "Sốt kéo dài": [
        ("Cảm cúm", "Sốt, ho, sổ mũi, đau mỏi người", "Nghỉ ngơi, uống nhiều nước, thuốc hạ sốt"),
        ("Viêm họng cấp", "Sốt nhẹ, đau họng, ho khan", "Kháng sinh, thuốc hạ sốt, súc họng nước muối"),
    ],
    "Ho kéo dài": [
        ("Viêm phế quản", "Ho kéo dài, khạc đờm, tức ngực", "Thuốc long đờm, kháng sinh nếu có nhiễm khuẩn"),
        ("Viêm xoang", "Nghẹt mũi, ho về đêm, chảy dịch mũi", "Xịt mũi, thuốc kháng viêm, rửa mũi nước muối"),
    ],
    "Đau bụng": [
        ("Viêm dạ dày", "Đau thượng vị, buồn nôn, ợ chua", "Thuốc giảm tiết acid, ăn uống đúng giờ"),
        ("Rối loạn tiêu hóa", "Đau bụng, tiêu chảy, đầy hơi", "Bù nước, men vi sinh, ăn nhẹ dễ tiêu"),
    ],
    "Mệt mỏi, chóng mặt": [
        ("Thiếu máu nhẹ", "Mệt mỏi, da xanh, hoa mắt", "Bổ sung sắt, ăn thực phẩm giàu sắt"),
        ("Rối loạn tiền đình", "Chóng mặt, buồn nôn, mất thăng bằng", "Thuốc tăng tuần hoàn não, tập vận động tiền đình"),
    ],
    "Đau lưng, đau khớp": [
        ("Đau thắt lưng", "Đau vùng lưng dưới, khó cúi người", "Thuốc giảm đau, vật lý trị liệu"),
        ("Thoái hóa khớp", "Đau khớp, cứng khớp buổi sáng", "Thuốc giảm đau kháng viêm, vận động nhẹ nhàng"),
    ],
}

GENERAL_DISEASES = [
    ("Sức khỏe bình thường", "Không có triệu chứng bất thường", "Không cần điều trị, tái khám định kỳ"),
    ("Tăng huyết áp", "Đau đầu, chóng mặt, mệt mỏi", "Thuốc hạ huyết áp, giảm muối, theo dõi huyết áp"),
    ("Đái tháo đường type 2", "Khát nước nhiều, tiểu nhiều, sụt cân", "Thuốc hạ đường huyết, chế độ ăn kiểm soát đường"),
    ("Dị ứng da", "Ngứa, nổi mẩn đỏ", "Thuốc kháng histamin, tránh tác nhân gây dị ứng"),
]

MEDICAL_NOTES = [
    "Bệnh nhân cần theo dõi huyết áp thường xuyên",
    "Tái khám sau 1 tuần nếu triệu chứng không giảm",
    "Bệnh nhân có tiền sử dị ứng thuốc, cần lưu ý khi kê đơn",
    "Hướng dẫn bệnh nhân uống thuốc đúng giờ",
    "Khuyên bệnh nhân nghỉ ngơi và uống nhiều nước",
    "Cần làm thêm xét nghiệm máu ở lần khám sau",
]

def get_completed_appointments_without_record(connection):
    query = text("""
        SELECT appointment_id, appointment_date, reason
        FROM appointment
        WHERE appointment_status = 'Completed'
            AND appointment_id NOT IN (SELECT appointment_id FROM medical_record)  
        """)
    return connection.execute(query).all()

def random_disease(reason):
    if reason in DISEASES_BY_REASON:
        return random.choice(DISEASES_BY_REASON[reason])
    else:
        return random.choice(GENERAL_DISEASES)

def random_notes():
    if random.random() < NOTES_RATE:
        return random.choice(MEDICAL_NOTES)
    else:
        return None

def build_record_data(appointment):
    appointment_id, appointment_date, reason = appointment
    diagnosis, symptoms, treatment = random_disease(reason)
    return {
        "appointment_id": appointment_id,
        "record_date": appointment_date,
        "diagnosis": diagnosis,
        "symptoms": symptoms,
        "treatment": treatment,
        "notes": random_notes(),
    }

def seed_medical_records():
    logger.info("Starting medical record seeding")

    with engine.begin() as connection:
        appointments = get_completed_appointments_without_record(connection)
        if not appointments:
            logger.info("No completed appointments without medical records found.")
            return

        record_data = [build_record_data(appointment) for appointment in appointments]

        insert_query = text("""
            INSERT INTO medical_record (
                appointment_id, 
                record_date,
                diagnosis,
                symptoms,
                treatment,
                notes
            ) VALUES (
                :appointment_id, 
                :record_date,
                :diagnosis,
                :symptoms,
                :treatment,
                :notes
            )
        """)
        connection.execute(insert_query, record_data)

    logger.info(f"Inserted {len(record_data)} medical records for completed appointments.")
    logger.info("Medical record seeding completed")

if __name__ == '__main__':
    setup_logging()
    seed_medical_records()
