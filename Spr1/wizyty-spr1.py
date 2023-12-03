# 20:37 - 23:31
# pełne godziny
# praca dentysty od 8:00 do 16:00


#--------------------TO DO-----------------------
# - sprawdzenie poprawności wprowadzania dat, godzin
# - dokończenie komend
# - godzina 08:00 i 09:00 <- brak '0' na początku


import os
file_path = "wizyty.txt"
visits = []
appointments = []
for i in range(8,16):
    appointments.append(f"{i}:00")
# print(appointments)

def validate_phone_number(phone_number):
    if phone_number.isdigit() and len(phone_number) == 9:
        return True
    return False

def check_file_exists(file_path):
    return os.path.exists(file_path)

def get_appointments_from_file(file_path):
    if check_file_exists(file_path):
        visits = []
        with open(file_path, "r") as file:
            for line in file:
                line = line.replace("\n","")
                line1 = line.split(";")
                visits.append(line1)
            return visits
    else:
        print("Brak pliku.")
        return visits

# Sprawdza, czy jest dostępny termin na podaną datę (max 8 wizyt na dzień)
def check_availability(appointments: str, date:str ):
    count = 8
    for visit in visits:
        if visit[1] == date:
            count -= 1
    if count >= 1:
        return True
    else:
        return False
    
def save_appointment(file_path, phone_number, date, time):
    visits = get_appointments_from_file(file_path)
    if validate_phone_number(phone_number) and check_availability(appointments, date):
        hours = show_available_hours(appointments,date) #available hours
        if time in hours:
            visits.append([phone_number,date,time])
            with open(file_path, "w") as file:
                for i in range(0,len(visits)):
                    file.write(f"{visits[i][0]};{visits[i][1]};{visits[i][2]}\n")
                return True
    return False

def show_available_hours(appointments,date):
    if check_file_exists(file_path):
        visits = get_appointments_from_file(file_path)
        hours = []  
        for visit in visits:
            if visit[1] == date:
                hours.append(visit[2].replace(":00",""))
        for h in hours: 
            if f"{h}:00" in appointments:
                appointments.remove(f"{h}:00")
        return appointments
        


# available_hours = show_available_hours(appointments,'05.11.2001')
# print(available_hours)


while True:
    print(" ")
    command = input("Enter command: ")
    print(" ")
    if command == "-g":
        visits = get_appointments_from_file(file_path)
    elif command =="-c":
        date = input("Enter date (dd:mm:yyyy): ")
        if check_availability(appointments, date):
            print("Visit available.")
        else:
            print("Visit unavailable.")
    elif command == "-s":
        phone_number = input("Enter phone number: ")
        date = input("Enter date (dd.mm.yyy):")
        print(show_available_hours(appointments,date))
        time = input("Enter time: ")
        if save_appointment(file_path, phone_number, date, time):
            print("Save visit.")
        else:
            print("Can't save visit.")
    elif command == "-show":
        date = input("Enter date (dd:mm:yyyy): ")
        t = show_available_hours(appointments,date)
        print("Available hours: ")
        print(t)
    elif command == "-e":
            break



# save_appointment(file_path, '112112112', '12.12.2023', '12:00')

# visits = [[phone_number, date], ...]

# visits = get_appointments_from_file(file_path)
# print(visits)
