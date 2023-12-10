def validate_phone_number(phone_number):
    return len(phone_number) == 9 and phone_number.isdigit()

def check_file_exists(file_path):
    try:
        with open(file_path):
            return True
    except FileNotFoundError:
        return False
    
def get_appointments_from_file(file_path):
    if check_file_exists(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()
    return []

def check_availability(appointments, date):
    return sum(date in appt for appt in appointments) < 8

    # [ lub ]
    # count = 0
    # for appt in appointments:
    #     if date in appt:
    #         count += 1
    # return count < 8


def save_appointment(file_path, phone_number, date, time):
    if not validate_phone_number(phone_number):
        print("Nieprawidłowy numer telefonu.")
        return False

    appointments = get_appointments_from_file(file_path)
    if not check_availability(appointments, date):
        print("Brak wolnych terminów na ten dzień.")
        return False

    with open(file_path, 'a') as file:
        file.write(f"{phone_number};{date};{time}\n")
    print("Wizyta została zapisana.")
    return False

def show_available_hours(appointments, date):
    if not check_availability(appointments, date):
        print("Brak wolnych terminów na ten dzień.")
        return
    
    working_hours = [f"{hour}:00" for hour in range(9,17)]

    booked_hours = [appt.split(';')[2].strip() for appt in appointments if date in appt]
    # [ lub ]
    # booked_hours = []
    # for appt in appointments:
    #     if date in appt:
    #         h = appt.split(';')[2].strip()
    #         booked_hours.append(h)

    available_hours = [hour for hour in working_hours if hour not in booked_hours]

    if available_hours:
        print("Dostępne godziny", ", ".join(available_hours))
    else:
        print("Brak wolnych terminów na ten dzień.")


file_path = "appointments.txt"
date = input("Podaj datę (YYYY:MM:DD): ")
appointments = get_appointments_from_file(file_path)
show_available_hours(appointments, date)
time = input("Podaj godzinę (HH24:MI): ")
phone_number = input("Podaj numer telefonu: ")
save_appointment(file_path, phone_number, date, time)