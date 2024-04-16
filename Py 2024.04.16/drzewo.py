# Drzewo

# drzewo - hierarchiczna struktura danych, naśladująca formę drzewa (odwróconego)

# korzeń - węzeł początkowy
# liść - element nie mający potomków
# głębokość drzewa - maksymalny poziom wszystkich elementów
# długość drogi wewnętrznej - liczba gałęzi od korzenia do liścia

#--------------------------------------------------------------------------------------

# Bezpośrednie odniesienie do węzłów dzieci:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Lista dzieci:

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


# Drzewo binarne:

tree = [1,2,3,4,5,6,7]

def get_left_child(index):
    """Zwraca lewe dziecko węzła o danym indeksie."""
    return 2 * index + 1

def get_right_child(index):
    """Zwraca prawe dziecko węzła o danym indeksie."""
    return 2 * index + 2

def get_parent(index):
    """Zwraca rodzica węzła o danym indeksie."""
    return (index - 1) // 2

# Dostęp do elementów drzewa
index = 0 # korzeń drzewa
left_child_index = get_left_child(index)
right_child_index = get_right_child(index)

print(f"Wartość korzenia: {tree[index]}")
print(f"Lewe dziecko korzenia: {tree[left_child_index]}")
print(f"Prawe dziecko korzenia: {tree[right_child_index]}")


# Odnośnik rodzic-dziecko:

"""
class Node:
    def __init__(self, data):
        ???
        
"""

# Rekurencyjne struktury danych


# Specjalny typ drzewa:

# -drzewo binarne (każdy węzeł ma maksymalnie 2 dzieci)
# -drzewa AVL
# -drzewa czerwono-czarne
# -kopce binarne


# Charakterystyka:

# -prosta struktura
# -zastosowanie (algorytmy sortowania, wyszukiwanie binarne, algorytmy graficzne)


# Rodzaje drzew binarnych 

# -drzewo binarne poszukiwań (BST) (po lewej mniejsze, po prawej większe; efektywne wyszukiwanie)
# -zbalansowane drzewo binarne
# -pełne drzewo binarne (każdy węzeł ma dokładnie 2 dzieci, oprócz liści)
# -kompletne drzewo binarne
# -doskonałe drzewo binarne


# Zastosowanie:

# -wyszukiwanie binarne
# -kopce
# -grafika komputerowa (drzewa BSP)
# -systemy baz danych (drzewa B+ i drzewa czerw-czarne)


# Przeglądanie węzłów drzewa

# -proces owiedzania każdego węzła raz


# Przeszukiwanie w głag (DFS):

# pre-order -> korzeń -> lewe poddrzewo -> prawe poddrzewo
# in-order (drzewa binarne) -> lewe poddrzewo -> korzeń -> prawe poddrzewo
# post-order

def dfs_preorder(node):
    if node:
        print(node.value) # Odwiedź korzeń
        dfs_preorder(node.left) # Przejście lewego poddrzewa
        dfs_preorder(node.right) # Przejście prawego poddrzewa



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_preorder(node):
    if node:
        print(node.value)
        dfs_preorder(node.left)
        dfs_preorder(node.right)


# Tworzenie drzewa
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Rozpoczęcie przeszukiwania w głąb (DFS) z korzenia
print("Przeszukiwanie w głąb (DFS) - Pre-order:")
dfs_preorder(root)



# Przeszukiwanie wszerz (BFS):

from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value)
        if current.left:
            queue.append(current.left)
        # if #???



# Eksploracja poziom po poziomie

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        print(current_node.value)

        if current_node.left is not None:
            queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Wywołanie przeszukiwania wszerz
print("Przeszukiwanie wszerz (BFS):")
bfs(root)




# Gdzie używamy drzew i algorytmów przeszukiwania?:

# -bazy danych
# -systemy plików
# -algorytmy sztucznej inteligencji
# -grafika komputerowa
# -algorytmy przeszukiwania ścieżek
# -struktury danych
# -kompilatory
# -analiza danych




#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Przeszukiwanie liniowe i przeszukiwanie binarne. Drzewa przeszukiwań binarnych.

#------------------------------------------------

# Przeszukiwanie liniowe:

# Zalety:
# -prostota implementacji
# -nie wymaga sortowania danych wejściowych

# Wady:
# -niska efektywność, zwłaszcza dla dużych zbiorów danych  O(n)


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         ...



#------------------------------------------------

# Przesukiwanie binerne

# Zalety:
# -wysoka efektywność dla posortowanych danych  O(log n)
# -znacznie szybsze niż przeszukiwanie liniowe dla dużych zbiorów danych

# Wady:
# -wymaga posortowanych danych
# -może nie być tak bardzo efektywne dla bardzo małych zbiorów danych lub danych, które nie mogą być łatwo posortowane



#------------------------------------------------

# Drzewo przeszukiwań binarnych (BST)

# Zalety:
# -efektywne wyszukiwanie, wstawianie i usuwanie - średnio O(log n)
# -struktura jest dynamiczna, może się dostosować i rosnąć w miarę dodawania

# Wady:
# -jeśli niezbilansowane mała złożoność (forma listy)  O(n)
# -wymaga dodatkowej pracy, aby utrzymać efektywność operacji w różnych przypadkach