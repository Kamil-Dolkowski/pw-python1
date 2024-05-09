# https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat

import sys

# print(sys.argv)     # zmienne systemowe

# sys.path.append("/path/to")

# sys.exit()      # wyjście z programu

# print(sys.version)
# print(sys.version_info)

with open('output.txt', 'w') as file:
    sys.stdout = file
    print('Hello World')

sys.stdout = sys.__stdout__

print(sys.platform)

# sys.stderr()    # przechwytuje errory ***