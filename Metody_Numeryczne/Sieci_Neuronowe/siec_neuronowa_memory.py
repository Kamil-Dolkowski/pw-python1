classes = [
    "Informatyka", 
    "Medycyna", 
    "Prawo", 
    "Lingwistyka", 
    "Psychologia", 
    "Matematyka", 
    "Budownictwo", 
    "Mechanika", 
    "Ekonomia", 
    "Architektura",
    "Muzyka"
]

properties = [
    "Umiejętności matematyczne",
    "Logiczne myślenie",
    "Zdolności językowe",
    "Kreatywność",
    "Umiejętność słuchania innych",
    "Empatia",
    "Dobra organizacja",
    "Dokładność",
    "Cierpliwość",
    "Odporność na stres",
    "Odpowiedzialność",
    "Zdolności manualne",
    "Wrażliwość artystyczna",
    "Czytanie ze zrozumieniem"
]

# Zakres wag: [0-5]

weights = [
    [4,5,4,5,1,0,5,5,5,5,3,0,0,4],
    [0,4,2,0,4,5,3,3,5,5,5,3,0,5],
    [1,5,3,2,3,1,4,5,4,3,5,0,0,5],
    [0,2,5,3,4,3,2,1,1,1,2,0,1,4],
    [2,5,3,3,5,5,2,2,5,2,5,0,0,3],
    [5,5,0,5,1,0,3,5,3,2,3,0,0,4],
    [5,4,1,4,1,0,5,5,4,3,5,0,0,3],
    [5,5,0,5,1,0,2,5,4,2,4,4,0,4],
    [5,5,3,3,1,0,5,5,4,2,4,0,0,5],
    [3,2,0,5,1,0,2,3,1,1,2,5,5,1],
    [1,2,1,5,3,4,5,4,5,5,2,4,5,3]
]


# Suma iloczynów
def sum_of_products(input: list[int], weights: list[int]) -> int :
    sum = 0

    for i in range(len(input)):
        sum += input[i] * weights[i]

    return sum


def main():
    input_values = []
    output = []
    final_answers = []

    print("Do poniższych cech wpisz oceny od 0 do 5, jak bardzo się do Ciebie odnoszą.\n")

    try:
        for property in properties:
            answer = int(input(f"{property}: "))

            if answer not in range(0,6):
                raise ValueError("Niepoprawna wartość")
            
            input_values.append(answer)
    except:
        print("\nBłąd: Wprowadzono niepoprawną wartość.")
        return
    
    # input_values = [4,4,3,5,4,5,4,5,3,4,4,5,5,4]
    # input_values = [5,5,5,5,5,5,5,5,5,5,5,5,5,5]

    for class_weights in weights:
        result = sum_of_products(input_values, class_weights)
        output.append(result)

    # print(output)

    output_with_classes = []

    for i in range(len(output)):
        output_with_classes.append((classes[i], output[i]))

    output_with_classes.sort(key = lambda x: x[1], reverse = True)
 
    for i in range(3):
        final_answers.append(output_with_classes[i])

    print("\n======= WYNIKI =======")
    print("(3 najlepsze kierunki)\n")
    for (field_of_study, value) in final_answers:
        print(f"{field_of_study}: {value}")

if __name__ == "__main__":
    main()
