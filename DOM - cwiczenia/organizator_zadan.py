# Organizator Zadań

# Cel Zadania:
# Zaprojektować i zaimplementować system organizacji zadań z użyciem drzewa binarnego, który pozwoli na efektywne planowanie i zarządzanie zadaniami.

# Opis Problemu:
# Osoba lub zespół potrzebuje narzędzia do zarządzania zadaniami, które umożliwi priorytetyzację zadań, ich szybkie dodawanie, edycję oraz usuwanie z bieżącej listy zadań.

# Struktura Drzewa:
# Każdy węzeł w drzewie reprezentuje jedno zadanie. Węzeł zawiera:

#     Unikalny identyfikator zadania,
#     Opis zadania,
#     Priorytet zadania (niższy numer oznacza wyższy priorytet),
#     Planowany termin wykonania.

# Wymagania Funkcjonalne:

#     Dodawanie Zadań: Możliwość dodania nowego zadania do listy.
#     Wyszukiwanie Zadań: Możliwość wyszukiwania zadań na podstawie ich identyfikatora lub priorytetu.
#     Aktualizacja Zadań: Możliwość aktualizacji opisu, priorytetu lub terminu wykonania zadania.
#     Usuwanie Zadań: Możliwość usunięcia zadania z listy.

class Node:
    def __init__(self, taskId, description, priority, realiseDate):
        self.taskId = taskId
        self.description = description
        self.priority = priority
        self.realiseDate = realiseDate
        self.left = None
        self.right = None

task = Node

# 1. Dodawanie Zadań:
def addTask(taskId, description, priority, realiseDate):
    global task
    # tworzenie 1 zadania
    if not isTask(task):
        # print("Brak zadań.")
        task = Node(taskId, description, priority, realiseDate)
        # print("Dodano 1 zadanie.")
        return 
    # dodawanie kolejnych zadań
    newTask = addTaskR(task, taskId, description, priority, realiseDate)
    # print("Dodano kolejne zadanie.")

    return newTask

def addTaskR(task, taskId, description, priority, realiseDate):
    if task is None:
        task = Node(taskId, description, priority, realiseDate)
        return task
    if taskId < task.taskId:
        task.left = addTaskR(task.left, taskId, description, priority, realiseDate)
    else:
        task.right = addTaskR(task.right, taskId, description, priority, realiseDate)

    return task

def isTask(task):
    try:
        if task.taskId:
            return True
    except AttributeError:
        return False
    






# 2. Wyszukiwanie Zadań:
def searchPrintTask(taskId, task):
    if not isTask(task):
        print(f"Brak zadań.")
        return 
    if taskId == task.taskId:
        print("\n======ZNALEZIONE ZADANIE======")
        print(f"Identyfikator: {task.taskId}")
        print(f"Opis: {task.description}")
        print(f"Priorytet: {task.priority}")
        print(f"Planowany termin wykonania: {task.realiseDate}\n")
    elif taskId < task.taskId:
        if not isTask(task.left):
            print(f"Brak zadania o identyfikatorze: {taskId}.")
            return 
        searchPrintTask(taskId, task.left)
    else:
        if not isTask(task.right):
            print(f"Brak zadania o identyfikatorze: {taskId}.")
            return 
        searchPrintTask(taskId, task.right)
    


def searchTask(taskId, task):
    if not isTask(task):
        print(f"Brak zadań.")
        return False
    if taskId == task.taskId:
        return True
    elif taskId < task.taskId:
        if not isTask(task.left):
            print(f"Brak zadania o identyfikatorze: {taskId}.")
            return False
        searchTask(taskId, task.left)
    else:
        if not isTask(task.right):
            print(f"Brak zadania o identyfikatorze: {taskId}.")
            return False
        searchTask(taskId, task.right)


# 3. Aktualizacja Zadań:
def updateTask(taskId, whatToChange, newData, task):
    if not isTask(task):
        print(f"Brak zadań.")
        return False
    if taskId == task.taskId:
        if whatToChange == 'description':
            print(f"Zaktualizowano opis: \nz: '{task.description}' \nna: '{newData}'\n")
            task.description = newData
        elif whatToChange == 'priority':
            print(f"Zaktualizowano priorytet: \nz: {task.priority} \nna: {newData}\n")
            task.priority = newData
        else:
            print(f"Zaktualizowano planowany termin wykonania: \nz: '{task.realiseDate}' \nna: '{newData}'\n")
            task.realiseDate = newData
        return True
    elif taskId < task.taskId:
        if not isTask(task.left):
            print(f"Brak zadania o identyfikatorze: {taskId}.")
            return False
        updateTask(taskId, whatToChange, newData, task.left)
    else:
        if not isTask(task.right):
            print(f"Brak zadania o identyfikatorze: {taskId}.")
            return False
        updateTask(taskId, whatToChange, newData, task.right)






# 4. Usuwanie Zadań:     ???
def deleteTask(taskId, task):
    if not isTask(task):
        print(f"Brak zadań.")
        return False
    
    
    if taskId == task.taskId:
        print(task.right)
        print(task.left)
        # brak liści
        if task.left == None and task.right == None:
            print("Usuń koniec")
            del task
            task = Node
            return task
        # są liście
        if task.left.taskId < task.right.taskId:
            print("są liście: l < p")
            task.taskId = task.left.taskId
            task.description = task.left.description
            task.priority = task.left.priority
            task.realiseDate = task.left.realiseDate
            task.left = task.left.left
            print(task.right.taskId)
            printTask(task)
            printTask(task.right)

        return task
            



    elif taskId < task.taskId:
        task.left = deleteTask(taskId, task.left)
    else:
        task.right = deleteTask(taskId, task.right)

    print("Koniec")
    # printTask(task)
    # printTask(task.left)
    # printTask(task.left.right)
    return task


    
def height(node):
    # Jeśli węzeł jest pusty, zwracamy -1, co oznacza brak węzła
    if node is None:
        return -1
    # Obliczamy wysokość lewego i prawego poddrzewa, dodając 1 do wyniku, aby uwzględnić obecny węzeł
    # Wysokość drzewa to maksymalna wysokość z 2 poddrzew + 1 dla bieżącego węzła
    else:
        left_height = height(node.left)
        right_height = height(node.right)

        return max(left_height, right_height) + 1

#-----------------------------------

def printTask(task):
    print(f"\n=====Analiza:=====")
    print(f"task.taskId: {task.taskId}")
    print(f"task.left: {task.left}")
    print(f"task.right: {task.right}\n")
    
def getIdList(task):
    idList = []
    
    if not isTask(task):
        return idList
    
    left = getIdList(task.left)
    right = getIdList(task.right)
    idList.append(task.taskId)

    return left + idList + right

def printCommands():
    print("=======POLECENIA=======")
    print("-h   lista poleceń")
    print("-a   dodaj zadanie")
    print("-s   znajdź zadanie")
    print("-u   zaktualizuj zadanie")
    print("-d   usun zadanie")
    print("-i   lista identyfikatorów zadań")
    print("-e   zakonczenie programu")
    print("")

#----------------------------------------

# addTask(4, 'opis3', 1, '2024-05-23')
# addTask(1, 'opis3', 1, '2024-05-23')

# searchPrintTask(4, task)
# addTask(2, 'opis2', 1, '2024-05-22')
# printTask(task)
# addTask(10, 'opis1', 1, '2024-05-21')
# printTask(task)
# printTask(task.left)
# addTask(5, 'opis3', 1, '2024-05-23')
# printTask(task)
# printTask(task.left)
# printTask(task.right)


addTask(5, 'opis3', 1, '2024-05-23')
addTask(2, 'opis3', 1, '2024-05-23')
addTask(3, 'opis2', 1, '2024-05-22')
addTask(1, 'opis2', 1, '2024-05-22')
# addTask(10, 'opis1', 1, '2024-05-21')
# addTask(5, 'opis3', 1, '2024-05-23')
print(f"idList = {getIdList(task)}\n")

task = deleteTask(1, task)
printTask(task)
printTask(task.left)
print(f"\nidList = {getIdList(task)}\n")

#----------------------------------------------------------

# printCommands()

while True:
    choice = input("--Podaj polecenie: ")
    print("")
    if choice == '-h':
        printCommands()
    elif choice == '-a':
        print("DODAWANIE ZADANIA:")
        taskId = int(input("Podaj identyfikator: "))
        description = input("Podaj opis: ")
        priority = input("Podaj priorytet: ")
        realiseDate = input("Podaj planowany termin wykonania: ")
        
        addTask(taskId, description, priority, realiseDate)
        print("\nDodano zadanie.\n")
    elif choice == '-s':
        print("SZUKANIE ZADANIA:")
        taskId = int(input("Podaj identyfikator: "))
        searchPrintTask(taskId, task)
    elif choice == '-u':
        taskId = int(input("Podaj identyfikator: "))
        whatToChange = input("Podaj, co chcesz zmienić [description/ priority/ realiseDate]: ")
        newData = input("Podaj, na co chcesz zmienić: ")
        print("")
        updateTask(taskId, whatToChange, newData, task)
    elif choice == '-d':
        pass
    elif choice == '-i':
        print("LISTA IDENTYFIKATORÓW ZADAŃ:")
        print(f"idList = {getIdList(task)}\n")
    elif choice == '-e':
        print("Zakończenie programu.\n")
        break
    else:
        print("Niepoprawne polecenie.")
        break
        


# Walidacja:

# if whatToChange == 'description':
        
# if whatToChange == 'priority':

# if whatToChange == 'releaseDate':
