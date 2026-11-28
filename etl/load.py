from pathlib import Path
from data_generator.database import engine
from sqlalchemy import text

SQL_DIR = Path("sql/etl")
LOADS = ["load_dim_department", "load_dim_doctor"]

def run_load(name):
    sql = (SQL_DIR / f"{name}.sql").read_text(encoding="utf-8")
    with engine.begin() as connection:
        connection.execute(text(sql))

if __name__ == "__main__":
    for name in LOADS:
        run_load(name)