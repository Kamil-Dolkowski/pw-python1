FILENAME = 'book.txt'

def read_phonebook():
    try:
        with open(FILENAME, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_phonebook(phonebook):
    with open(FILENAME, 'w') as file:
        # for entry in phonebook:
        file.write(f"{phonebook}\n")
        print("Save file.")

def display_phonebook():
    for list in read_phonebook():
        print(list)

def validate_number(phone_number:str ):
    return len(phone_number) == 9 and phone_number.isdigit()


def add_entry(name:str, phone_number:str ):
    if not phone_number.isdigit() or len(phone_number) != 9:
        print("Invalid phone number.")
        return
    add_new = f"{name}; {phone_number}"
    save_phonebook(add_new)
    print("Added phone number.")

def remove_entry(phone_number):
    save_phonebook([entry for entry in read_phonebook() if  phone_number not in entry])
    # OPCJONALNIE:
    # new_list = []
    # for entry in read_phonebook():
    #   if phone_number not in entry:
    #       new_list.append(entry)
    # save_phonebook(new_list)
            

def modify_entry(old_phone_number, new_name, new_phone_number):
    if not validate_number(new_phone_number):
        print("Invalid phone number.")
        return False
    lista = read_phonebook()
    for key,row in enumerate(lista):
        if old_phone_number in row:
            lista[key] = f"{new_name}; {new_phone_number}"
            save_phonebook(lista)
            print("Save")
            return True


while True:
    print("0. Exit")
    choice = input("Enter instr: ")
    if choice == '0':
        print("Exit")
        
        break

# read_phonebook()
# add_entry('name', '123456789')
# display_phonebook()
# # remove_entry('123456789')

# modify_entry('123456789', 'aaa', '987654321')
# display_phonebook()

# display_phonebook()
# add_entry('name', '123456789')
# display_phonebook()
# print(read_phonebook())