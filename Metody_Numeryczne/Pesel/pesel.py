def validate_pesel(pesel) -> bool :
    if pesel.isdigit() == False:
        print("\nBłąd: PESEL musi składać się wyłącznie z cyfr")
        return False
    
    if len(pesel) != 11:
        print("\nBłąd: Nieprawidłowa długość (PESEL ma 11 cyfr)")
        return False
    
    if date_validate(pesel) == False:
        print("\nBłąd: Niepoprawny numer PESEL")
        return False
    
    if int(pesel[10]) != control_digit(pesel):
        print("\nBłąd: Niepoprawny numer PESEL")
        return False
    
    return True

def date_validate(pesel) -> bool :
    month = int(month_of_birth_number(pesel))
    if month > 12 or month == 0:
        return False
    
    day = int(day_of_birth(pesel))
    two_last_digits_of_year = int(pesel[0:2])
    if day == 0:
        return False
    if month in [1,3,5,7,8,10,12]:
        if day > 31:
            return False
    elif month == 2: # luty
        if two_last_digits_of_year % 4 == 0:
            # rok przestępny
            if day > 29:
                return False
        else:
            # rok zwykły
            if day > 28:
                return False
    else:
       if day > 30:
            return False 
    
    return True


def control_digit(pesel) -> int :
    control_digit = 0
    weights = [1,3,7,9,1,3,7,9,1,3]

    for i in range(0, len(pesel)-1):
        control_digit += (int(pesel[i]) * weights[i]) % 10

    control_digit = 10 - (control_digit % 10)

    return control_digit

def day_of_birth(pesel) -> str :
    return pesel[4:6]

def month_of_birth_number(pesel) -> str :
    month = int(pesel[2:4]) % 20

    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    return month

def month_of_birth_word(pesel) -> str :
    months = {
        "01": "Styczeń",
        "02": "Luty",
        "03": "Marzec",
        "04": "Kwiecień",
        "05": "Maj",
        "06": "Czerwiec",
        "07": "Lipiec",
        "08": "Sierpień",
        "09": "Wrzesień",
        "10": "Październik",
        "11": "Listopad",
        "12": "Grudzień"
    }

    month = month_of_birth_number(pesel)
    return months[month]

def year_of_birth(pesel) -> str :
    centuries = {
        1800: [8,9],
        1900: [0,1],
        2000: [2,3],
        2100: [4,5],
        2200: [6,7]
    }

    two_last_digits_of_year = pesel[0:2]
    month = pesel[2:4]

    for (century, first_digit) in centuries.items():
        for digit in first_digit:
            if int(month[0]) == digit:
                year = century + int(two_last_digits_of_year)
                return str(year)

def date_of_birth(pesel):
    day = day_of_birth(pesel)
    month = month_of_birth_number(pesel)
    year = year_of_birth(pesel)

    return f"{day}-{month}-{year}"

def sex_short_value(pesel):
    sex_digit = int(pesel[9])
    if sex_digit % 2 == 0:
        return 'K'
    else:
        return 'M'

def sex_long_value(pesel):
    sex_digit = int(pesel[9])
    if sex_digit % 2 == 0:
        return "Kobieta"
    else:
        return "Mężczyzna"

# ================================

def main():
    pesel = input("Wprowadź numer PESEL: ")

    if validate_pesel(pesel):
        print("\nPoprawny numer PESEL")
        print(f"\nDzień: {day_of_birth(pesel)}")
        print(f"Miesiąc: {month_of_birth_number(pesel)} | {month_of_birth_word(pesel)}")
        print(f"Rok: {year_of_birth(pesel)}")
        print(f"Data urodzenia: {date_of_birth(pesel)}")
        print(f"Płeć: {sex_short_value(pesel)} | {sex_long_value(pesel)}")
        print(f"Cyfra kontrolna: {control_digit(pesel)}")

if __name__ == "__main__":
    main()