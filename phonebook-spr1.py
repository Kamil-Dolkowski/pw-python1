file_path = "phonebook.txt"
phonebook = []


# funkcja, która pobiera dane z pliku i wyświetla jako tablicę
def read_phonebook():
    try:
        with open(file_path, "r") as file:
            phonebook = []
        with open(file_path, "r") as file:
            for line in file:
                line1 = line.replace("\n","")
                line1 = line1.split(" ")
                phonebook.append(line1)
            print("Wczytano z pliku: \n")
            print(phonebook)
            return phonebook
    except FileNotFoundError: 
        print("Brak pliku.")
            
def save_phonebook():
    with open(file_path, "w") as file:
        for i in range(0,len(phonebook)):
            file.write(f"{phonebook[i][0]} {phonebook[i][1]}\n")
        return phonebook

def display_phonebook():
    print(phonebook)

def add_entry(name,phone_number: str):
    # sprawdzenie czy numer jest liczbą i ma 9 cyfr
    if not phone_number.isdigit() or len(phone_number) != 9:
        print("Błędny numer telefonu.")
    else:
    # sprawdzenie, czy nie ma już takiego numeru tel.
        for i in phonebook:
            if i[1] == phone_number:
                print("Już jest taki numer telefonu.")
                return phonebook
        phonebook.append([name,phone_number])  
        print(" ")
        print(f"Dodano: {name} {phone_number} do phonebook'a.")
        return phonebook

def modify_entry(old_phone_number,new_name,new_phone_number):
    # sprawdzenie czy numer jest liczbą i ma 9 cyfr
    if not new_phone_number.isdigit() or len(new_phone_number) != 9:
        print("Błędny numer telefonu.")
    else:
        for i in phonebook:
            if i[1] == old_phone_number:
                old_name = i[0]
                i[1] = new_phone_number
                i[0] = new_name
                return old_name, phonebook
        print("Brak takiego numeru telefonu.")

def remove_entry(phone_number):
    for i in phonebook:
        if i[1] == phone_number:
            id = phonebook.index(i)
            del phonebook[id]
            return
    return print("Brak telefonu do usunięcia.")





while True:
    print(" ")
    command = input("Enter command: ")
    print(" ")
    if command == '-l':
        phonebook = read_phonebook()
    elif command == '-s':
        phonebook = save_phonebook()
        print("Zapisano do pliku.")
    elif command == '-d':
        print("Phonebook: ")
        display_phonebook()
    elif command == '-a':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        phonebook = add_entry(name,phone_number)
    elif command == '-r':
        phone_number = input("Enter phone number: ")
        remove_entry(phone_number)
        print("")
        print(f"Usunięto telefon o numerze '{phone_number}' z phonebook'a.")
    elif command == '-m':
        old_phone_number = input("Enter old phone number: ")
        new_phone_number = input("Enter new phone number: ")
        new_name = input("Enter new name: ")
        print("")
        old_name, phonebook = modify_entry(old_phone_number, new_name, new_phone_number)
        print(f"Zmieniono: {old_name} {old_phone_number} na: {new_name} {new_phone_number}.")
    elif command == '-h':
        print("-l   read_phonebook()")
        print("-s   save_phonebook()")
        print("-d   display_phonebook()")
        print("-a   add_entry()")
        print("-r   remove_entry()")
        print("-m   modify_entry()")
        print("-h   help")
        print("-e   exit\n")
        
    elif command == '-e':
        print("Zakończono pracę programu.\n")
        break


# read_phonebook()
# add_entry('weronika','110373333')
# save_phonebook()
# print(phonebook)
# remove_entry('110373333')

# phonebook = [['kamil','12345'],['wieslaw','50567']]
# save_phonebook()
