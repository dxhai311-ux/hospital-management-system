import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

# 1. Read database configuration
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# 2. Validate required configuration
required_config = {
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
    "DB_HOST": DB_HOST,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
}

missing_config = [
    name
    for name, value in required_config.items()
    if not value
]

if missing_config:
    raise RuntimeError(
        "Missing required environment variables: "
        + ", ".join(missing_config)
    )

# 3. Validate the port
try:
    DB_PORT = int(DB_PORT)
except ValueError:
    raise RuntimeError("DB_PORT must be an integer.")

if not 1 <= DB_PORT <= 65535:
    raise RuntimeError("DB_PORT must be between 1 and 65535")

# 4. Build the database URL safely
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

# 5. Create the SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)