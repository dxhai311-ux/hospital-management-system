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

OBSERVATION_PARTS = [
    "Huyết áp và mạch trong giới hạn bình thường.",
    "Huyết áp hơi cao so với lần khám trước.",
    "Khám lâm sàng chưa thấy dấu hiệu bất thường khác.",
    "Bệnh nhân tỉnh táo, tiếp xúc tốt.",
    "Thể trạng trung bình, không sốt tại thời điểm khám.",
    "Bệnh nhân có tiền sử dị ứng thuốc, cần lưu ý khi kê đơn.",
]

ADVICE_PARTS = [
    "Khuyên bệnh nhân nghỉ ngơi và uống nhiều nước.",
    "Hướng dẫn bệnh nhân uống thuốc đúng giờ sau bữa ăn.",
    "Hạn chế đồ ăn cay nóng và rượu bia trong thời gian điều trị.",
    "Ngủ đủ giấc, tránh thức khuya.",
    "Theo dõi nhiệt độ và huyết áp tại nhà mỗi ngày.",
    "Tránh làm việc nặng trong vài ngày tới.",
]

FOLLOW_UP_PARTS = [
    "Tái khám sau 1 tuần nếu triệu chứng không giảm.",
    "Tái khám ngay nếu xuất hiện sốt cao hoặc đau tăng.",
    "Cần làm thêm xét nghiệm máu ở lần khám sau.",
    "Hẹn tái khám sau 2 tuần để đánh giá lại.",
    "Tái khám định kỳ mỗi tháng.",
    "Nếu ổn định, tiếp tục theo dõi tại nhà.",
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

def random_notes(diagnosis, symptoms, treatment):
    if random.random() < NOTES_RATE:
        base =  f"Bệnh nhân khám vì {symptoms}. Chẩn đoán: {diagnosis}. Hướng điều trị: {treatment}."
        all_parts = OBSERVATION_PARTS + ADVICE_PARTS + FOLLOW_UP_PARTS
        extra_count = random.randint(0, 3)
        extras = random.sample(all_parts, extra_count)
        return " ".join([base] + extras)
        
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
        "notes": random_notes(diagnosis, symptoms, treatment),
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
