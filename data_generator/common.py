import random
from datetime import timedelta

LAST_NAMES = ["Đặng", "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Phan", "Vũ", "Đỗ", "Bùi", "Lưu", "Tạ", "Đinh", "Trịnh", "Trương"]
MALE_MIDDLE_NAMES = ["Xuân", "Quang", "Văn", "Hữu", "Minh"]
FEMALE_MIDDLE_NAMES = ["Thị", "Thúy", "Thu", "Thùy", "Kim"]
MALE_FIRST_NAMES = ["Hải", "Huy", "Quân", "Hùng", "Nam", "Phúc", "Dương", "Đức", "Dũng", "Long", "Bảo", "Đăng", "Phong", "Sang", "Tuấn", "Đô", "Khôi", "Kiên", "Cường", "Lâm", "Vinh", "Thuận", "Bắc", "Kiệt", "Thành"]
FEMALE_FIRST_NAMES = ["Hạnh", "La", "Hương", "Ngân", "Mai", "Thảo", "Trang", "Vy", "Linh", "Hà", "Phương", "Quỳnh", "Nhung", "Diễm", "Thủy", "Bích", "Trâm", "Yến", "Huyền", "Duyên", "Thư", "My", "Ngọc", "Diệp", "Lan"]

def random_gender():
    return random.choice(["Male", "Female"])

def build_full_name(gender):
    last_name = random.choice(LAST_NAMES)
    if gender == "Male":
        middle_name = random.choice(MALE_MIDDLE_NAMES)
        first_name = random.choice(MALE_FIRST_NAMES)
    else:
        middle_name = random.choice(FEMALE_MIDDLE_NAMES)
        first_name = random.choice(FEMALE_FIRST_NAMES)

    return f"{last_name} {middle_name} {first_name}"

def random_phone_number():
    number = random.randint(10000000, 99999999)
    return f"09{number}"

def random_date_between(start, end):
    total_days = (end - start).days
    n = random.randint(0, total_days)
    return start + timedelta(days=n)
