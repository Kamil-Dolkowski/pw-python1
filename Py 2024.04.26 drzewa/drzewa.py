# Zrozumienie znaczenia i metod balansowania drzew binarnych.

# 1. Co to balansowanie drzewa?
# 2. AVL
# 3. Drzewa czerwono-czarne
# 4. Zastosowania i korzyści

#---------------------------------------------------------------------------------------------------------------------------

# Balansowanie drzewa - utrzymanie wysokiej wydajności operacji wyszukiwania, wstawiania i usuwania

# O(log n) - zbalansowane
# O(n) - niezbalansowane

#---------------------------------------------------------------------------------------------------------------------------

# Dlaczego balans jest ważny?:

# Niezbalansowane przybiera formę "długiej linii" (każdy węzeł ma 1 dziecko), operacje są nieefektywne jak u zwykłej listy

#---------------------------------------------------------------------------------------------------------------------------

# Zadanie BTS:

# 8,2,5,14,1,10,12,13,6,9


# 1,2,5,6,8,9,10,12,13,14
#         ^


#              8
#             / \
#            /   \
#           2     9
#          / \     \
#         1   5     14
#              \    / 
#               6  10
#                  /\
#                 9  12
#                      \
#                      13

#- - - - - - - - - - - - - - - - - - - - - - 

# Drzewa AVL:

#              8     (2-3)
#             / \
#            /   \
#    (1-1)  5     13     (2-1)
#          / \    / \
#   (0)   2   6  10 14    (0)
#               /  \   
#       (0)    9   12   (0)


# BTS - optymalizuje czas wyszukiwania elementów w zbiorze liczb

# ścieżka poszukiwań jes tco najwyżej tak długa jak h - wysokość drzewa BST


# minimum - skrajnie lewy węzeł
# maksimum - skrajnie prawy węzeł

#- - - - - - - - - - - - - - - - - - - - - - 

# Metody przechodzenia wszystkich elem. drzewa:
# -pre-order (wzdłużna): korzeń, lewe poddrzewo, prawe poddrzewo
# -in-order (poprzeczna): lewe poddrzewo, korzeń, prawe poddrzewo
# -post-order (wsteczna): lewe poddrzewo, prawe poddrzewo, korzeń ( złożoność O(n) )  (do usuwania i dodawania)

#---------------------------------------------------------------------------------------------------------------------------

# Zad. 1

#              4
#            /   \
#           2     8
#          / \   / \ 
#         1   3 6   9
#              / \
#             5   7  

# Metody przechodzenia:
# -pre-order:  4,2,1,3,8,6,5,7,9
# -in-order:   1,2,3,4,5,6,7,8,9
# -post-order: 1,3,2,5,7,6,9,8,4

#- - - - - - - - - - - - - - - - - - - - - - 

# Zad. 2

#                        9
#                   /        \
#                  2          15
#                 / \         /
#                1   4       11
#                     \     /  \
#                      8   10  13
#                     /        / \
#                    5        12  14
#                     \
#                      7


# Metody przechodzenia:
# -pre-order:  9,2,1,4,8,5,7,15,11,10,13,12,14
# -in-order:   1,2,4,5,7,8,9,10,11,12,13,14,15
# -post-order: 1,7,5,8,4,2,10,12,14,13,11,15,9


#---------------------------------------------------------------------------------------------------------------------------


# -usuwanie liścia
# -usuwanie elementu, który ma 1 potomka
# -usuwanie elementu, który ma 2 węzły potomne




# AVL
# -wysokość n-elementowego drzewa AVL wynosi O(log n)
# -drzewo jest zrównoważone
# -współczynnik wyważenia - różnica wysokości lewego i prawego poddrzewa (0,+1 lub -1)
# -jeśli współczynnik ma 2 lub -2 to drzewo straciłow łasność AVL, potrzeba rotacji, maksymalnie 2 rotacje
