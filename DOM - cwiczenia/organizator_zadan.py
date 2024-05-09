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
        # printTask(task)       ## Dane o sąsiadach tego węzła
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


# 4. Usuwanie Zadań:
def deleteTask(taskId, task):
    if not isTask(task):
        print("Brak zadań.\n")
        return task
    
    # korzeń
    if taskId == task.taskId:
        # brak liści I
        if task.left == None and task.right == None:
            del task
            task = Node
            print("Usunięto zadanie.\n")
            return task
        # jest 1 liść II
        elif task.left == None:
            task = task.right
            print("Usunięto zadanie.\n")
            return task
        elif task.right == None:
            task = task.left
            print("Usunięto zadanie.\n")
            return task
        # są 2 liście III
        else:
            rightSide = task.right
            task.left = task.left.left

            if isTask(task.right):   # czy task ma coś po prawej stronie
                maxRightTask = maxRight(task)
                maxRightTask.right = rightSide
            else:
                task.right = rightSide

            print("Usunięto zadanie.\n")
            return task
        
    # lewa strona
    if isTask(task.left):
        if taskId == task.left.taskId:
            # brak liści I
            if task.left.left == None and task.left.right == None:
                del task.left
                task.left = None
                print("Usunięto zadanie.\n")
                return task
            # jest 1 liść II
            if task.left.right == None: 
                task.left = task.left.left
                print("Usunięto zadanie.\n")
                return task
            if task.left.left == None:
                task.left = task.left.right
                print("Usunięto zadanie.\n")
                return task
            # są 2 liście III
            rightSide = task.left.right     # rightSide - prawa gałąź od usuwanego elementu 
            task.left = task.left.left

            if isTask(task.left.right):   # czy task.left ma coś po prawej stronie
                maxRightTask = maxRight(task.left)
                maxRightTask.right = rightSide
            else:
                task.left.right = rightSide
            print("Usunięto zadanie.\n")
            return task

    # prawa strona
    if isTask(task.right):
        if taskId == task.right.taskId:
            # brak liści I
            if task.right.left == None and task.right.right == None:
                del task.right
                task.right = None
                print("Usunięto zadanie.\n")
                return task
            # jest 1 liść II
            if task.right.right == None: 
                task.right = task.right.left
                print("Usunięto zadanie.\n")
                return task
            if task.right.left == None:
                task.right = task.right.right
                print("Usunięto zadanie.\n")
                return task
            # są 2 liście III
            rightSide = task.right.right
            task.right = task.right.left

            if isTask(task.right.right):   # czy task.right.right ma coś po prawej stronie
                maxRightTask = maxRight(task.right)
                maxRightTask.right = rightSide
            else:
                task.right.right = rightSide
            print("Usunięto zadanie.\n")
            return task

    # brak takiego zadania 
    if task.left == None and task.right == None:
        print("Nie znaleziono zadania do usunięcia.\n")
        return task

    if taskId < task.taskId:
        task.left = deleteTask(taskId, task.left)
        return task
    else:
        task.right = deleteTask(taskId, task.right)
        return task
    
def maxRight(task):
    if isTask(task.right):
        maxRightTask = maxRight(task.right)
        return maxRightTask
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

def printTaskObj(task):
    print(f"\n=====Analiza:=====")
    print(f"task.taskId: {task.taskId}")
    print(f"task.left: {task.left}")
    print(f"task.right: {task.right}\n")
    
def printTask(task):
    if isTask(task):
        print(f"=====Analiza:=====")
        print(f"task.taskId: {task.taskId}")
        if isTask(task.left):
            print(f"task.left: {task.left.taskId}")
        else:
            print(f"task.left: {task.left}")
        if isTask(task.right):
            print(f"task.right: {task.right.taskId}")
        else:
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
    print("-p   wydrukuj drzewo zadań")
    print("-e   zakonczenie programu")
    print("")


def rightRotation(task):
    leftTask = task.left
    task.left = leftTask.right
    leftTask.right = task
    task = leftTask
    return task

def leftRotation(task):
    rightTask = task.right
    task.right = rightTask.left
    rightTask.left = task
    task = rightTask
    return task




# rozprostowanie drzewa
def bilans1(task):
    if isTask(task.left):
        task = rightRotation(task)
        task = bilans1(task)
    if isTask(task.right):
        task.right = bilans1(task.right)
    
    return task

def bilansNumber(n):
    x = n + 1

# Algorytm DSW
def bilans_(task):
    # rozprostowanie drzewa
    task = bilans1(task)
    n = height(task) + 1
    print(f"n = {n}")
    x = n + 1
    x = 2 << 1
    print(x)

    return task



# drzewo AVL
def balans(task):
    leftHeight = height(task.left) 
    rightHeight = height(task.right) 
    print(f"{leftHeight} {rightHeight}")
    if abs(leftHeight - rightHeight) > 1:
        if leftHeight > rightHeight:
            # LL
            if height(task) == 2 and isTask(task.left.left):
                task = rightRotation(task)
                return task
            # LP
            if height(task) == 2 and isTask(task.left.right):
                task.left = leftRotation(task.left)
                task = rightRotation(task)
                return task
        elif leftHeight < rightHeight:
            #PP
            if height(task) == 2 and isTask(task.right.right):
                task = leftRotation(task)
                return task
            #PL
            if height(task) == 2 and isTask(task.right.left):
                task.right = rightRotation(task.right)
                task = leftRotation(task)
                return task
            
    if isTask(task.left):
        task.left = balans(task.left)
    if isTask(task.right):
        task.right = balans(task.right)

    return task
            


def printTree(task):
    printTask(task)
    try:
        printTree(task.left)
    except AttributeError:
        pass
    try:
        printTree(task.right)
    except AttributeError:
        pass

#----------------------------------------

addTask(7, 'opis3', 1, '2024-05-23')
print("7")
task = balans(task)
printTree(task)
addTask(4, 'opis3', 1, '2024-05-23')
print("4")
task = balans(task)
printTree(task)
addTask(5, 'opis2', 1, '2024-05-22')
print("5")
task = balans(task)
printTree(task)
addTask(6, 'opis2', 1, '2024-05-22')
print("6")
task = balans(task)
printTree(task)
addTask(2, 'opis1', 1, '2024-05-21')
print("2")
task = balans(task)
printTree(task)

addTask(1, 'opis3', 1, '2024-05-23')
print("1")
task = balans(task)
printTree(task)
addTask(3, 'opis3', 1, '2024-05-23')
print("3")
task = balans(task)
printTree(task)
addTask(10, 'opis2', 1, '2024-05-22')
print("10")
task = balans(task)
printTree(task)


# addTask(11, 'opis1', 1, '2024-05-21')
# addTask(9, 'opis3', 1, '2024-05-23')
# addTask(8, 'opis3', 1, '2024-05-23')
# print(f"idList = {getIdList(task)}\n")

# printTask(task)



# task = rightRotation(task)
# task = leftRotation(task)

# printTree(task)
# print("---------------------------------")
# task = balans(task)
print("=================================")
printTree(task)

#----------------------------------------------------------

printCommands()

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
        task = balans(task)
        print("\nDodano zadanie.\n")
    elif choice == '-s':
        print("SZUKANIE ZADANIA:")
        taskId = int(input("Podaj identyfikator: "))
        searchPrintTask(taskId, task)
    elif choice == '-u':
        print("AKTUALIZACJA ZADANIA:")
        taskId = int(input("Podaj identyfikator: "))
        whatToChange = input("Podaj, co chcesz zmienić [description/ priority/ realiseDate]: ")
        newData = input("Podaj, na co chcesz zmienić: ")
        print("")
        updateTask(taskId, whatToChange, newData, task)
    elif choice == '-d':
        print("USUWANIE ZADANIA:")
        taskId = int(input("Podaj identyfikator: "))
        print("")
        task = deleteTask(taskId, task)
        # task = balans(task)
    elif choice == '-i':
        print("LISTA IDENTYFIKATORÓW ZADAŃ:")
        print(f"idList = {getIdList(task)}\n")
    elif choice == '-p':
        printTree(task)
    elif choice == '-e':
        print("Zakończenie programu.\n")
        break
    else:
        print("Niepoprawne polecenie.")
        break
        


# UWAGI:
# -brak walidacji wprowadzanych danych
# -błędy po balansie drzewa (po usunięciu węzła)




#-----------------------------------------------------

# Walidacja:

# if whatToChange == 'description':
        
# if whatToChange == 'priority':

# if whatToChange == 'releaseDate':
