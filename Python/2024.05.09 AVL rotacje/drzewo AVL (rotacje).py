# Balans drzewa

#-------------------------------------------DRZEWO AVL--------------------------------------------------

# Rotacje: (4 rodzaje)
# -2 pojedyncze
# -2 podwójne




# Rotacja RR lub LL:

#   1                               
#     \                             2
#       2            ->           /   \      
#         \                     1       3
#            3

# węzeł 1 -> lewy potomek węzła 2
# węzeł 2 -> węzeł 1

# -zachowana kolejność

# Rotacja RL lub LR:

#   1
#     \
#       2
#       /
#     3      

# LL - węzły 2 i 3, potem RR - węzły 1 i 2


#------------------------------ZADANIE--------------------------------

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # Wysokość węzła inicjalnie ustawiona na 1

def update_height(node):
    # Aktualizacja wysokości węała na podstawie wysokości jego dzieci.
    node.height = max(height(node.left), height(node.right)) + 1

def height(node):
    # Pobieranie wysokości węzła, jeśli węzeł nie istnieje zwróc 0.
    if not node:
        return 0

    return node.height


def left_rotate(x):
    # Wykonanie rotacji w lewo na węźle x
    y = x.right
    T2 = y.left

    # Przeprowadzenie rotacji
    y.left = x
    x.right = T2

    # Aktualizacja wysokości po rotacji
    update_height(x)
    update_height(y)
    
    # Nowy korzeń po rotacji
    return y


def right_rotate(y):
    # Wykonanie rotacji w prawo na węźle y
    x = y.left
    T2 = x.right

    # Przeprowadzenie rotacji
    x.right = y
    y.left = T2

    # Aktualizacja wysokości po rotacji
    update_height(x)
    update_height(y)

    # Nowy korzeń po rotacji
    return x


def right_left_rotate(node):
    # Pierwsza rotacja - lewa rotacja na prawym dziecku
    node.right = right_rotate(node.right)
    # Druga rotacja - prawa rotacja na węźle
    return left_rotate(node)





#------------------------

# Użycie:
# Załóżmy, że mamy drzewo AVL i potrzebujemy wykonać rotację w prawo na węźle 'y'
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print(root.key)
# Wykonanie rotacji w prawo
root = right_rotate(root)
print(root.key)


