import argparse

# $ pip install argparse

parser = argparse.ArgumentParser(
    description="Program do wyswietlania listy plików"
)

parser.add_argument('echo', help='wyswietlenie stringa')
parser.add_argument('-v', help='wiecej danych o output', action='store_true')

args = parser.parse_args()

