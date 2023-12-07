import datetime

class Wizyty:

    def __init__(self, file_path="appointments.txt") -> None:   #konstruktor
        self.file_path = file_path

    # static method - nieistotny dla działania klasy, walidacja, żadnych zmian na tym, wewnątrz innych funkcji
    @staticmethod
    def validate_phone_number(self, phone_number: str) -> bool:
        return len(phone_number) == 9 and phone_number.isdigit()


    def check_file_exists(self):
        try:
            with open(self.file_path):
                return True
        except FileNotFoundError:
            return False
        

    def get_appointments_from_file(self):
        if self.check_file_exists():
            with open(self.file_path, 'r') as file:
                return file.readlines()
        return []

    def check_availability(self, appointments:list, date:str) -> bool:
        try:
            datetime.datetime.strptime(date, "%Y:%m:%d")
        except ValueError:
            print("Nieprawidłowy format daty.")
            return False
        return sum(date in appt for appt in appointments) < 8
    
    def save_appointment(self, phone_number, date, time):
        if not self.validate_phone_number(phone_number):
            print("Nieprawidłowy numer telefonu.")
            return False

        appointments = self.get_appointments_from_file()
        if not self.check_availability(appointments, date):
            print("Brak wolnych terminów na ten dzień.")
            return False

        with open(self.file_path, 'a') as file:
            file.write(f"{phone_number};{date};{time}\n")
        print("Wizyta została zapisana.")
        return False

    def show_available_hours(self, date):
        appointments = self.get_appointments_from_file()
        if not self.check_availability(appointments, date):
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

wizyty1 = Wizyty()

date = input("Podaj datę (YYYY:MM:DD): ")
wizyty1.show_available_hours(date)
time = input("Podaj godzinę (HH24:MI): ")
phone_number = input("Podaj numer telefonu: ")
wizyty1.save_appointment(phone_number, date, time)
