class phonebook:

    def __init__(self, filename='book1.txt') -> None:        # konstruktor
        self.filename = filename
        self.phonebook = self.read_phonebook()

    def read_phonebook(self):
        phonebook = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split('; ')
                    phonebook[phone_number] = name
        except FileNotFoundError:
            print("Brak pliku")
        return phonebook    

    def save_phonebook(self):
        with open(self.filename, 'w') as file:
            for phone_number, name in self.phonebook.items():
                file.write(f"{name}; {phone_number}\n")
        print("Phonebook saved.")

    def display_phonebook(self):
        self.phonebook = self.read_phonebook()
        for phone_number, name in self.phonebook.items():
            print(f"{name}: {phone_number}")

    def validate_number(self, phone_number):
        return len(phone_number) == 9 and phone_number.isdigit()

    def add_entry(self, name, phone_number):
        if not self.validate_number(phone_number):
            print("Invalid phone number.")
            return
        phonebook = self.read_phonebook()
        if phone_number in phonebook:
            print("Phone number already exists.")
            return
        self.phonebook[phone_number] = name
        self.save_phonebook()
        print("Phone number added.")

    def remove_entry(self, phone_number):
        self.phonebook = self.read_phonebook()
        if phone_number in self.phonebook:
            del self.phonebook[phone_number]
            self.save_phonebook()
            print("Phone number removed.")
        else:
            print("Phone number not found.")

    def modify_entry(self, old_phone_number, new_name, new_phone_number):
        self.phonebook = self.read_phonebook()
        if old_phone_number not in self.phonebook:
            print("Old phone number not found.")
            return False
        if not self.validate_number(new_phone_number):
            print("Niepoprawny numer.")






phonebook1 = phonebook()
# phonebook1.filename1 = 'ksiazka.txt'
# phonebook1.filename = 'book2.txt.txt'
phonebook1.read_phonebook()
phonebook1.add_entry("Krzysztof", "123456789")
phonebook1.display_phonebook()
# phonebook1.modify_entry("123456789","Anna", "987654321")
phonebook1.remove_entry("123456789")
phonebook1.display_phonebook()
# phonebook2 = Phonebook('phone.txt')

# print(phonebook1.read_phonebook())
# print(phonebook2)