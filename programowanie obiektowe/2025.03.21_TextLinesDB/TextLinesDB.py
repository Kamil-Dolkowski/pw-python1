from abc import ABC, abstractmethod
from datetime import datetime
import sqlite3

# class TextLines(ABC):
#     @abstractmethod
#     def get_number_of_lines(self):
#         pass

#     @abstractmethod
#     def read_line(self, line_number):
#         pass

#     @abstractmethod
#     def write_line(self, text):
#         pass

#     @abstractmethod
#     def write_line(self, text, line_number):
#         pass

#     @abstractmethod
#     def delete_line(self, line_number):
#         pass

## Python nie obsługuje (bezpośrednio) przeciążeń !!

class TextLines(ABC):
    # BEGIN: Public methods
    @abstractmethod
    def get_number_of_lines(self):
        pass

    @abstractmethod
    def read_line(self, line_number):
        pass

    @abstractmethod
    def delete_line(self, line_number):
        pass

    @abstractmethod
    def write_line(self, text, line_number = None):
        pass

    '''
    def write_line(self, text, line_number = None):
        if line_number is None:
            self.__write_line_at_end(text)
        else:
            self.__write_line_at_index(text, line_number)

    # BEGIN: Private methods

    @abstractmethod
    def __write_line_at_end(self, text):
        pass

    @abstractmethod
    def __write_line_at_index(self, text, line_number):
        pass
    '''

class TextLinesInMemory(TextLines):
    # BEGIN: Public methods
    def __init__(self):
        self.__lines = []

    def get_number_of_lines(self):
        return len(self.__lines)

    def read_line(self, line_number):
        # # 1. Lepsze z obiektowego punktu widzenia
        if line_number < self.get_number_of_lines():
            return self.__lines[line_number]
        else:
            raise IndexError("Line number out of range")
        
        # # 2. Lepsze z niskopoziomowego punktu widzenia (możliwie szybsza)
        # if line_number < len(self.__lines):
        #     return self.__lines(line_number)

    def delete_line(self, line_number):
        if line_number >= 0 and line_number < self.get_number_of_lines():
            self.__lines[line_number] = ""
        else:
            raise IndexError("Line number out of range")

    def write_line(self, text, line_number = None):
        if line_number is None:
            self.__write_line_at_end(text)
        else:
            self.__write_line_at_index(text, line_number)

    # BEGIN: Private methods
    def __write_line_at_end(self, text):
        if type(text) is not str:
            raise TypeError("Text must be a string")
        
        self.__lines.append(text)

    def __write_line_at_index(self, text, line_number):
        if type(text) is not str:
            raise TypeError("Text must be a string")
        
        # 1. koncepcja (konserwatywna)
        '''
        if line_number >= 0 and line_number < self.get_number_of_lines():
            self.__lines[line_number] = text
        else:
            raise IndexError("Line number out of range")
        '''

        # 2. koncepcja (postępowa)
        if line_number >= 0 and line_number < self.get_number_of_lines():
            self.__lines[line_number] = text
        else:
            for _ in range(line_number - self.get_number_of_lines()):
                self.__write_line_at_end("")
            self.__write_line_at_end(text)

    def dump(self):
        print(self.__lines)

class IdentifiedTextLines:
    # BEGIN: Public methods
    def __init__(self):
        self.__lines = TextLinesInMemory()
        self.__ids = {}

    def get_identifiers(self):
        return [id for id in self.__ids]

    def write_line(self, text, identifier):
        if identifier not in self.__ids:
            self.__ids[identifier] = []

        self.__lines.write_line(text)
        line_number = self.__lines.get_number_of_lines() - 1

        self.__ids[identifier].append(line_number)

    def read_line(self, identifier):
        if identifier not in self.__ids:
            raise KeyError("Unknown identifier")
        
        result = []

        for idx in self.__ids[identifier]:
            line = self.__lines.read_line(idx)
            result.append(line)

        return result
    
    def delete_line(self, identifier):
        if identifier not in self.__ids:
            raise KeyError("Unknown identifier")
        
        for idx in self.__ids[identifier]:
            self.__lines.delete_line(idx)

        del self.__ids[identifier]

    def find_free_index(self):
        number_of_lines = self.__lines.get_number_of_lines()
        print(number_of_lines)
        
        seq = [n for n in range(number_of_lines)]
        print(seq)

        for key in self.__ids:
            print(f"Identifier {key}")
            for idx in self.__ids[key]:
                seq.remove(idx)
        
        print(seq)
        
        if len(seq) > 0:
            print(f"Use index {seq[0]}")
        else:
            print("Use without index (append)")
        

    def dump(self):
        self.__lines.dump()

# Uwaga! Tutaj indeksacja wierszy jest od 1.
class TextLinesInDB(TextLines):
    # BEGIN: Public methods
    def __init__(self, db_name = None):
        if db_name is None:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%s")
            self.__db_name = f"data_{timestamp}.db"
        else: 
            self.__db_name = db_name

        connection = sqlite3.connect(self.__db_name)

        with open("db.sql") as script:
            connection.executescript(script.read())

        connection.commit()
        connection.close()

        self.__connection = None
        self.__cursor = None

    def get_number_of_lines(self):
        sql = "SELECT COUNT(*) AS count FROM lines"

        connection = self.__get_connection()
        connection.row_factory = sqlite3.Row

        cur = connection.cursor()
        res = cur.execute(sql)
        row = res.fetchone()
        row = dict(row)

        # connection.close()

        return row['count']

    def read_line(self, line_number):
        # # 1. Lepsze z obiektowego punktu widzenia
        if line_number <= self.get_number_of_lines():
            sql = "SELECT * FROM lines WHERE id=(?)"

            connection = self.__get_connection()
            connection.row_factory = sqlite3.Row

            cur = connection.cursor()
            res = cur.execute(sql, (line_number, ))
            row = res.fetchone()
            row = dict(row)

            # connection.close()

            return row
        else:
            raise IndexError("Line number out of range")
        
        # # 2. Lepsze z niskopoziomowego punktu widzenia (możliwie szybsza)
        # if line_number < len(self.__lines):
        #     return self.__lines(line_number)

    def delete_line(self, line_number):
        if line_number >= 1 and line_number <= self.get_number_of_lines():
            sql = "UPDATE lines SET line = '', modiffied = CURRENT_TIMESTAMP WHERE id = (?)"

            connection = self.__get_connection()

            cur = connection.cursor()
            res = cur.execute(sql, (line_number, ))

            connection.commit()
            # connection.close()
        else:
            raise IndexError("Line number out of range")

    def write_line(self, text, line_number = None):
        if line_number is None:
            self.__write_line_at_end(text)
        else:
            self.__write_line_at_index(text, line_number)

    # BEGIN: Private methods
    def __write_line_at_end(self, text):
        if type(text) is not str:
            raise TypeError("Text must be a string")
        
        sql = "INSERT INTO lines (line) VALUES (?)"

        connection = self.__get_connection()

        cur = connection.cursor()
        res = cur.execute(sql, (text,))

        connection.commit()
        # connection.close()

    def __write_line_at_index(self, text, line_number):
        if type(text) is not str:
            raise TypeError("Text must be a string")
        
        # 1. koncepcja (konserwatywna)
        '''
        if line_number >= 0 and line_number < self.get_number_of_lines():
            self.__lines[line_number] = text
        else:
            raise IndexError("Line number out of range")
        '''

        # 2. koncepcja (postępowa)
        if line_number >= 1 and line_number <= self.get_number_of_lines():
            sql = "UPDATE lines SET line = (?), modiffied = CURRENT_TIMESTAMP WHERE id = (?)"

            connection = self.__get_connection()

            cur = connection.cursor()
            res = cur.execute(sql, (text, line_number))

            connection.commit()
            # connection.close()
        else:
            for _ in range(1, line_number - self.get_number_of_lines()):
                self.__write_line_at_end("")
            self.__write_line_at_end(text)

    def __get_connection(self):
        if self.__connection is None:
            self.__connection = sqlite3.connect(self.__db_name)
        return self.__connection
    
    def closeDB(self):
        self.__connection.close()
        self.__connection = None

    def dump(self):
        sql = "SELECT * FROM lines"

        connection = self.__get_connection()
        connection.row_factory = sqlite3.Row

        cur = connection.cursor()
        res = cur.execute(sql)
        rows = res.fetchall()

        for row in rows:
            print(dict(row))

        # connection.close()

# ==================================================================


def test_TextLinesInMemory():
    tlim = TextLinesInMemory()

    line_number = tlim.get_number_of_lines()
    print(line_number)

    tlim.write_line("test text")
    line_number = tlim.get_number_of_lines()
    print(line_number)

    tlim.write_line("foo bar",5)
    line_number = tlim.get_number_of_lines()
    print(line_number)
    
    tlim.write_line("baz bar",2)
    line_number = tlim.get_number_of_lines()
    print(line_number)

    line = tlim.read_line(2)
    print(line)

    tlim.delete_line(2)
    line_number = tlim.get_number_of_lines()
    print(line_number)

    line = tlim.read_line(2)
    print(line)

    try:
        line = tlim.read_line(20)
        print(line)
    except IndexError:
        print("Bad index")


def test_IdentifiedTextLines():
    itl = IdentifiedTextLines()
    itl.write_line("foo 1", "f1")
    itl.write_line("bar 1", "b1")
    itl.write_line("foo 2", "f1")
    itl.write_line("bar 2", "b1")
    itl.write_line("foo 3", "f1")

    itl.dump()
    
    lines = itl.read_line("f1")
    for l in lines:
        print(l)

    ids = itl.get_identifiers()
    print(ids)

    itl.delete_line("f1")

    itl.dump()

    itl.find_free_index()

def test_TextLinesInDB():
    tlidb = TextLinesInDB("line_set.db")

    number_of_lines = tlidb.get_number_of_lines()
    print(number_of_lines)

    tlidb.write_line("Tekst 1")
    tlidb.write_line("Tekst 2")
    tlidb.write_line("Tekst 3")

    number_of_lines = tlidb.get_number_of_lines()
    print(number_of_lines)

    line = tlidb.read_line(2)
    print(line)

    tlidb.write_line("Modyfikacja 2",2)

    line = tlidb.read_line(2)
    print(line)

    tlidb.closeDB()

    tlidb.delete_line(2)

    line = tlidb.read_line(2)
    print(line)

    tlidb.write_line("Tekst 5",5)

    line = tlidb.read_line(4)
    print(line)

    line = tlidb.read_line(5)
    print(line)

    number_of_lines = tlidb.get_number_of_lines()
    print(number_of_lines)

    tlidb.dump()

def main():
    # test_TextLinesInMemory()
    # test_IdentifiedTextLines()
    test_TextLinesInDB()

if __name__ == "__main__":
    main()