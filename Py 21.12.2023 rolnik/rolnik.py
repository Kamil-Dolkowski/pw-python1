

def calculate_field_area(length: float, width: float) -> float:
    return length * width

def format_fields_data(fields):
    # [(20,50), (44,80)]
    return ", ".join([(f"{l}x{w}") for l,w in fields])
   

def write_fields_data_to_file(filename, farmer, fields_data):
    with open(filename, "a") as file:
        file.write(f"{farmer}; {fields_data}\n")


def calculate_total_area(fields_data):
    # 50x60, 44x80
    fields = fields_data.strip().split(",")
    total = 0
    for field in fields:
        l,w = map(float, field.split("x"))
        total += calculate_field_area(l,w)
        return total

def read_and_display_fields_data(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                farmer, fields_data = line.strip().split(";")
                field = fields_data.strip().split(",")
                total_area = calculate_total_area(fields_data)
                print(f"Rolnik: {farmer}, Działki: {fields_data}, Lączna powierzchnia: {total_area} m^2")
    except FileNotFoundError:
        print("File not found.")
    return


def main():
    farmer_name = "Jan Kowalski"
    filename = "fields_data.txt"
    fields = [(60,20),(55,26)]  



    # farmer_name = "Jan Kowalski"
    # filename = "fields_data.txt"
    # fields = [(60,20),(55,26)]
    f_fields = format_fields_data(fields)
    write_fields_data_to_file(filename, farmer_name, f_fields)
    # format_fields_data([(20,50), (44,80)])
    read_and_display_fields_data(filename)


if __name__ == '__main__':      # zabezpieczenie w razie wywołania modułu -> main się nie wykona
    main()
    a