import os
import random
from timeit import default_timer as timer

def generate_data(file_path, size, max_value):
    with open(file_path, "w") as file_out:
        for _ in range(size-1):
            number = random.randint(0, max_value)
            file_out.write(str(number) + "\n")
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

def get_all_files_in_directory(working_directory):
    files = []

    for file in os.listdir(working_directory):
        file_path = os.path.join(working_directory, file)

        if not os.path.isdir(file_path):
            files.append(file)

    return files

def sort_data_in_directory(working_directory):
    files = get_all_files_in_directory(working_directory)

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
    safe = 10

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

                

def main():
    begin = timer()

    clear_directory("work")

    # generate_data("data.dat", 10, 20)

    divide_file("data.dat", 3, "work")

    sort_data_in_directory("work")

    # merge_two_files("work", "data_1.dat", "data_2.dat", "data_1_2.dat")

    merge_all_files("work")

    end = timer()
    print(f"Time: {end - begin} s")

if __name__ == "__main__":
    main()