# Zad. 1
# Obliczanie wysokości drzewa.

class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None



def height(node):   # rekurencyjna
    # Jeśli węzeł jest pusty, zwracamy -1, co oznacza brak węzła
    if node is None:
        return -1
    # Obliczamy wysokość lewego i prawego poddrzewa, dodając 1 do wyniku, aby uwzględnić obecny węzeł
    # Wysokość drzewa to maksymalna wysokość z 2 poddrzew + 1 dla bieżącego węzła
    else:
        left_height = height(node.left)
        right_height = height(node.right)

        return max(left_height, right_height) + 1






# Dane:
#        10
#     5      20
#  3       15   30
#                  32


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.right.left = Node(15)
root.right.right = Node(30)
# root.right.right.left = Node(31)
root.right.right.right = Node(32)

print(height(root))




# Zad.2
# Funkcja, która sprawdza, czy dane drzewo binarne jest zbalansowane. Drzewo uważa się za zbilansowane, jeśli dla każdego węzła różnica wysokości jego poddrzew lewego i prawego nie przekracza 1.

# root.left.left.left = Node(1)         # <- drzewo niezbalansowane
# root.right.right.right.right = Node(40)       # <- drzewo niezbalansowane (inna opcja)

# # mój kod:
# def isBinary(node):
#     if node is None:
#         print("Drzewo zbilansowane")
#     else:
#         left_height = height(node.left)
#         right_height = height(node.right)

#         if -1 >= (left_height - right_height) <= 1:
#             print("Drzewo zbilansowane.")
#         else:
#             print("Drzewo niezbilansowane.")


# Pana kod:
def balans(node):
    if node is None:
        return True
    
    left_height = height(node.left)
    right_height = height(node.right)

    if abs(left_height - right_height) > 1:
        return False
    else:
        return balans(node.left) and balans(node.right)




#isBinary(root)

print(balans(root))
    




# Zad.3
# Stwórz program lub skrypt, który pozwoli wizualizować drzewo binarne. Użytkownik powinien móc podać ciąg operacji wstawiania.

# ** Stwórz program lub skrypt, który pozwoli wizualizować efekt rotacji pojedynczej i podwójnej na drzewie binarnym. Użytkownik powinien móc podać ciąg operacji wstawiania, a następnie zobaczyć jak drzewo jest transformowane przez rotacje.


def wizualizuj(node):
    root = node.value

    if node.left != None:
        left = node.left.value
    else:
        left = None

    if node.right != None:
        right = node.right.value
    else:
        right = None

    if left == None and right == None:
        print(f"        {root}         ")
    elif left == None :
        print(f"        {root}         ")
        print(f"               {right} ")
    elif right == None:
        print(f"        {root}         ")
        print(f" {left}                ")
    else:
        print(f"        {root}         ")
        print(f"     {left}      {right}")

    print("")


    wizualizuj(node.left)




    # print(f"        {root}         ")
    # print(f"  {left}      {right}")
    

wizualizuj(root)





# Zastosowania drzew binarnych:
# -rozkład masy (np. w samolocie, na statku) [system rezerwacji biletów do samolotu]



# system rezerwacji biletów do samolotu (prawo, lewo, przód, tył [balans] )   <- na zaliczenie ??
