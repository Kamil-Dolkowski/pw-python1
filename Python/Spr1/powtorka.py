# 18:08 - 19:25
from datetime import datetime
FILENAME = "wizyty1.txt"


# nr_tel; day; hour

def validate_phone_number(phone_number: str) -> bool:
    return phone_number.isdigit() and len(phone_number) == 9

def check_file_exists(file_path):
    try:
        with open(file_path, "r") as file:
            return True
    except FileNotFoundError:
        print("File not exists.")
        return False

def get_appointments_from_file(file_path):
    if not check_file_exists(file_path):
        return []
    visits = []
    with open(file_path, "r") as file:
        for line in file:
            visit = line.strip().split(";")
            visits.append(visit)
    return visits

def check_availability(file_path, date):
    visits = get_appointments_from_file(file_path)
    count = 0
    for visit in visits:
        if visit[1] == date:
            count+=1
    if count < 8:
        return True
    return False

def save_appointment(file_path, phone_number, date, time):
    if not check_file_exists(file_path):
        return 
    if not validate_phone_number(phone_number):
        print("Invalid phone number.")
        return
    if not check_availability(file_path, date):
        return
    if not validate_time(time):
        print("Invalid time.")
        return
    available_hours = show_available_hours(file_path, date)
    if time not in available_hours:
        print("Unavailable hour.")
        return
    with open(file_path, "a") as file:
        file.write(f"{phone_number};{date};{time}\n")
    print("Appointment saved.")    
    return

def show_available_hours(file_path, date):
    visits = get_appointments_from_file(file_path)
    hours = [f"{i}:00" for i in range(8,16)]
    available_hours = hours
    for visit in visits:
        if visit[1] == date:
            available_hours.remove(visit[2])
    return available_hours

def validate_date(date) -> bool:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format.")
        return False

def validate_time(time):
    hours = [f"{i}:00" for i in range(8,16)]
    if time in hours:
        return True
    return False

if check_file_exists(FILENAME):
    date = input("Enter date (YYYY-MM-DD): ")
    if validate_date(date):
        print("Available hours: ")
        print(show_available_hours(FILENAME, date))
        time = input("Enter time (HH:MM): ")
        phone_number = input("Enter phone number: ")
        save_appointment(FILENAME, phone_number, date, time)

