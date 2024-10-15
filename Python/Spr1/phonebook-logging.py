import logging

# Konfiguracja logowania
logging.basicConfig(filename='phonebook.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Phonebook:
    def __init__(self, filename='book.txt'):
        self.filename = filename
        self.phonebook = {}
        self.load_phonebook()

    def load_phonebook(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split('; ')
                    self.phonebook[phone_number] = name
        except FileNotFoundError:
            logging.warning(f"File {self.filename} not found. A new phonebook will be created.")
        except Exception as e:
            logging.error(f"An error occurred while loading the phonebook: {e}")

    def save_phonebook(self):
        try:
            with open(self.filename, 'w') as file:
                for phone_number, name in self.phonebook.items():
                    file.write(f"{name}; {phone_number}\n")
            logging.info("Phonebook saved successfully.")
        except Exception as e:
            logging.error(f"An error occurred while saving the phonebook: {e}")

    def display_phonebook(self):
        for phone_number, name in self.phonebook.items():
            print(f"{name}: {phone_number}")

    def validate_number(self, phone_number):
        return len(phone_number) == 9 and phone_number.isdigit()

    def add_entry(self, name, phone_number):
        if not self.validate_number(phone_number):
            logging.warning("Attempted to add an invalid phone number.")
            return False
        if phone_number in self.phonebook:
            logging.warning("Attempted to add a phone number that already exists.")
            return False
        self.phonebook[phone_number] = name
        self.save_phonebook()
        return True

    def remove_entry(self, phone_number):
        if phone_number not in self.phonebook:
            logging.warning("Attempted to remove a phone number that does not exist.")
            return False
        del self.phonebook[phone_number]
        self.save_phonebook()
        return True

    def modify_entry(self, old_phone_number, new_name, new_phone_number):
        if old_phone_number not in self.phonebook:
            logging.warning("Attempted to modify a phone number that does not exist.")
            return False
        if not self.validate_number(new_phone_number):
            logging.warning("Attempted to modify to an invalid phone number.")
            return False
        del self.phonebook[old_phone_number]
        self.phonebook[new_phone_number] = new_name
        self.save_phonebook()
        return True

# Użycie klasy
phonebook = Phonebook()
phonebook.add_entry("Krzysztof", "123456789")
phonebook.display_phonebook()
phonebook.modify_entry("123456789", "Ania", "000000000")
phonebook.remove_entry("123456789")
phonebook.display_phonebook()