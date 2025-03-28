import os
import random
from timeit import default_timer as timer

def generate_data(file_path, size, max_value):
    with open(file_path, "w") as file_out:
        for i in range(size-1):
            number = random.randint(0, max_value)
            file_out.write(str(number) + "\n")
            if i % 100_000 == 0:
                print(f"{i} of {size}")
        number = random.randint(0, max_value)
        file_out.write(str(number))

def divide_file(file_path, size, working_directory):
    with open(file_path, "r") as file_data:
        file_number = 1
        end = False

        while not end:
            file_out_name = f"data_{file_number}.dat"
            file_out_path = os.path.join(working_directory, file_out_name)
            file_number += 1
            counter = 0

            line = file_data.readline().strip()
            if not line:
                break

            with open(file_out_path, "w") as file_out:
                file_out.write(line)
                counter += 1

                while counter < size:
                    line = file_data.readline().strip()
                    if not line:
                        end = True
                        break

                    file_out.write("\n" + line)
                    counter += 1

            if file_number % 10 == 0:
                print(f"{file_number} of {size}")

def get_all_files_in_directory(working_directory):
    files = []

    for file in os.listdir(working_directory):
        file_path = os.path.join(working_directory, file)

        if not os.path.isdir(file_path):
            files.append(file)

    return files

def sort_data_in_directory(working_directory):
    files = get_all_files_in_directory(working_directory)
    c = 1
    number_of_files = len(files)

    for file in files:
        file_path = os.path.join(working_directory, file)
        data = None

        with open(file_path, "r") as source_file:
            data = [int(line.strip()) for line in source_file]

        data.sort()

        with open(file_path, "w") as result_file:
            for i in range(len(data)-1):
                result_file.write(str(data[i]) + "\n")
            result_file.write(str(data[-1]))

        if c % 10 == 0:
            print(f"{c} of {number_of_files}")

        c += 1

def merge_two_files(working_directory, file_in_1_name, file_in_2_name, file_out_name):
    file_in_1_path = os.path.join(working_directory, file_in_1_name)
    file_in_2_path = os.path.join(working_directory, file_in_2_name)
    file_out_path = os.path.join(working_directory, file_out_name)

    with open(file_in_1_path, "r") as file_in_1:
        with open(file_in_2_path, "r") as file_in_2:
            with open(file_out_path, "w") as file_out:
                line_1 = file_in_1.readline().strip()
                line_2 = file_in_2.readline().strip()

                while True:
                    if line_1 and line_2:
                        v1 = int(line_1)
                        v2 = int(line_2)

                        if v1 < v2:
                            file_out.write(str(v1))
                            line_1 = file_in_1.readline().strip()
                        else:
                            file_out.write(str(v2))
                            line_2 = file_in_2.readline().strip()
                    elif line_1 and not line_2:
                        file_out.write(line_1)
                        line_1 = file_in_1.readline().strip()
                    elif not line_1 and line_2:
                        file_out.write(line_2)
                        line_2 = file_in_2.readline().strip()
                    else:
                        break

                    if line_1 or line_2:
                        file_out.write("\n")
    
def merge_one_iteration(working_directory, files, iteration, remove_source_files = True):
    dim = 2
    list_of_pairs = [files[i:i+dim] for i in range(0,len(files),dim)]

    p = 1

    for pair in list_of_pairs:
        if len(pair) == dim:
            file_in_1_name = pair[0]
            file_in_2_name = pair[1]
            file_out_name = f"{iteration}_{p}.dat"

            merge_two_files(working_directory, file_in_1_name, file_in_2_name, file_out_name)
        else:
            path_current = os.path.join(working_directory, pair[0])
            path_new = os.path.join(working_directory, f"{iteration}_{p}.dat")
            os.rename(path_current, path_new)
        
        p += 1

    if remove_source_files:
        for file in files:
            file_path = os.path.join(working_directory, file)
            if not os.path.isdir(file_path):
                if os.path.exists(file_path):
                    os.remove(file_path)

def merge_all_files(working_directory):
    files = get_all_files_in_directory(working_directory)
    number_of_files = len(files)

    iteration = 1
    safe = 100

    while number_of_files > 1 and safe > 0:
        safe -= 1
        merge_one_iteration(working_directory, files, iteration, True)
        files = get_all_files_in_directory(working_directory)
        number_of_files = len(files)
        iteration += 1

def clear_directory(working_directory):
    files = get_all_files_in_directory(working_directory)

    for file in files:
        file_path = os.path.join(working_directory, file)
        if not os.path.isdir(file_path):
            if os.path.exists(file_path):
                os.remove(file_path)


# ================================================

def check_lengths_of_files(original_file_name, working_directory):
    files = get_all_files_in_directory(working_directory)
    original_file_length = 0
    sorted_file_length = 0

    if len(files) != 1:
        raise NameError("Too many files.")
    
    with open(original_file_name, "r") as original_file:
        if original_file.readline():
            original_file_length += 1

    sorted_file_name = os.path.join(working_directory, files[0])
    with open(sorted_file_name, "r") as sorted_file:
        if sorted_file.readline():
            sorted_file_length += 1

    if original_file_length == sorted_file_length:
        return True
    else:
        return False

def check_numbers_in_files(original_file_name, working_directory):
    files = get_all_files_in_directory(working_directory)
    numbers = {}

    if len(files) != 1:
        raise NameError("Too many files.")

    with open(original_file_name, "r") as original_file:
        for line in original_file:
            number = line.strip()
            if not number in numbers:
                numbers[number] = 0
            numbers[number] += 1

    sorted_file_name = os.path.join(working_directory, files[0])
    with open(sorted_file_name, "r") as sorted_file:
        for line in sorted_file:
            number = line.strip()
            if not number in numbers:
                numbers[number] = 0
            numbers[number] -= 1

    for number in numbers.values():
        if number != 0:
            return False
        
    return True

def is_sorted(working_directory):
    files = get_all_files_in_directory(working_directory)
    sorted_file_name = os.path.join(working_directory, files[0])

    if len(files) != 1:
        raise NameError("Too many files.")

    with open(sorted_file_name, "r") as sorted_file:
        x = int(sorted_file.readline().strip())

        for line in sorted_file:
            y = int(line.strip())
            if x > y:
                return False
            x = y
            
        return True




def main():
    clear_directory("work")

    begin = timer()
    # generate_data("data_test.dat", 1_000_000, 2_000_000)
    generate_data("data_test.dat", 4, 20)
    end = timer()
    print(f"Generate time: {end - begin} s")
    
    begin = timer()
    divide_file("data_test.dat", 4, "work")
    end = timer()
    print(f"Divide time: {end - begin} s")

    begin = timer()
    sort_data_in_directory("work")
    end = timer()
    print(f"Sort time: {end - begin} s")

    begin = timer()
    merge_all_files("work")
    end = timer()
    print(f"Merge time: {end - begin} s")
    
    # ======================================

    print("\n========= Sprawdzenie =========")

    begin = timer()

    # result = check_lengths_of_files("data_test.dat", "work")
    # print(f"Ta sama długość plików: {result}")

    result = check_numbers_in_files("data_test.dat", "work")
    print(f"Te same ilości liczb: \t{result}")
    
    result = is_sorted("work")
    print(f"Dane posortowane: \t{result}")

    end = timer()
    print(f"\nCheck time: {end - begin} s")

if __name__ == "__main__":
    main()