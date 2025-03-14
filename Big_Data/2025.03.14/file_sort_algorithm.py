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

def sort_data_in_directory(working_directory):
    file_paths = []

    for f in os.listdir(working_directory):
        file_path = os.path.join(working_directory, f)

        if not os.path.isdir(file_path):
            file_paths.append(file_path)

    for file_path in file_paths:
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
    



                

def main():
    begin = timer()

    # generate_data("data.dat", 10, 20)

    # divide_file("data.dat", 3, "work")

    # sort_data_in_directory("work")

    # merge_two_files("work", "data_1.dat", "data_2.dat", "data_1_2.dat")

    end = timer()
    print(f"Time: {end - begin} s")

if __name__ == "__main__":
    main()