import subprocess
import sys
import os
import shutil
import importlib.util

REQUIRED_TOOLS = ["python", "flyway"]
REQUIRED_FILES = ["flyway.toml", ".env"]
REQUIRED_PACKAGES = ["sqlalchemy", "pandas", "dotenv", "psycopg2"]

GENERATORS = [
    'department',
    'patient',
    'medicine',
    'doctor', 
    'room',
    'appointment',
    'medical_record',
    'prescription',
    'prescription_item',
    'invoice', 
    'payment'
]

def run(command):
    print(f"Running : {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as error:
        print("Error : ", error)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Command not found : {command[0]}")
        sys.exit(1)
    
def run_generators():
    for name in GENERATORS:
        command = ["python", "-m", f"data_generator.generators.{name}"]
        run(command)

def check_tools():
    for tool in REQUIRED_TOOLS:
        if shutil.which(tool) is None:
            print(f"Tool not installed : {tool}")
            sys.exit(1)

def check_files():
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            print(f"Missing file : {file}")
            sys.exit(1)

def check_packages():
    for package in REQUIRED_PACKAGES:
        if importlib.util.find_spec(package) is None:
            print(f"Package not installed : {package}")
            sys.exit(1)

def rebuild():
    flyway = shutil.which("flyway")
    run([flyway, "-cleanDisabled=false", "clean"])
    run([flyway, "migrate"])
    run_generators()
    run(["python", "-m", "data_generator.dirty_data"])

if __name__ == "__main__":
    check_tools()
    check_packages()
    check_files()
    print("This will delete ALL data in the database. Confirmation required!")
    answer = input("Type YES to continue, NO to cancel : ").strip().upper()
    if answer == 'YES':
        rebuild()
    else:
        print("Cancelled!")