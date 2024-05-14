# Zadanie
# System zarządzania rezerwacjami lotów

# Struktura drzewa: Każdy węzeł drzewa reprezentuje jedną rezerwację. Węzeł zawiera:
# -ID rezerwacji (unikalny id)
# -imie i nazwisko pasażera
# -data lotu

# Wymagania funkcjonalne:
# -dodawanie rezerwacji: na podst. ID rezerwacji
# -wyszukiwanie rezerwacji: na podst. ID, zawiera dane rezerwacji
# -usuwanie rezerwacji:

#--------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, reservation_id: int, passenger_name: str, flight_date: str):
        self.reservation_id = reservation_id
        self.passenger_name = passenger_name
        self.flight_date = flight_date
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, reservation_id: int, passenger_name: str, flight_date: str):
        # Jeśli drzewo jest puste
        if self.root is None:
            self.root = Node(reservation_id, passenger_name, flight_date)
        else:
            self._insert(self.root, reservation_id, passenger_name, flight_date)
    
    def _insert(self, current_node: Node, reservation_id: int, passenger_name: str, flight_date: str):
        # metoda wstawiania nowej rezerwacji do odpowiedniego węzła

        # jeśli ID rezerwacji jest mniejsze niż ID aktualnego węzła przejdź w lewo
        if reservation_id < current_node.reservation_id:
            if current_node.left is None:
                # jeśli lewe drzewo jest puste, wstaw tutaj nowy węzeł
                current_node.left = Node(reservation_id, passenger_name, flight_date)
            else:
                # w przeciwnym razie wywołaj rekurencyjną funkcję _insert dla lewego dziecka
                self._insert(current_node.left, reservation_id, passenger_name, flight_date)
        elif reservation_id > current_node.reservation_id:
            # jeśli ID rezerwacji jest większe niż ID aktualnego węzła przejdź w prawo
            if current_node.right is None:
                # jeśli prawe drzewo jest puste, wstaw tutaj nowy węzeł
                current_node.right = Node(reservation_id, passenger_name, flight_date)
            else:
                # w przeciwnym razie wywołaj rekurencyjną funkcję _insert dla prawego dziecka
                self._insert(current_node.right, reservation_id, passenger_name, flight_date)
        else:
            # w przeciwnym razie rezerwacja już istnieje
            print("Rezerwacja już istnieje!")
        

    # Szukamy i zwracamy węzeł po danym ID rezerwacji
    def find(self, reservation_id: int):
        # Jeśli drzewo jest puste
        if self.root is None:
            print("Brak rezerwacji.")
        else:
            return self._find(self.root, reservation_id)
        
    def _find(self, current_node: Node, reservation_id: int):
        if current_node:
            if reservation_id == current_node.reservation_id:
                return current_node
            elif reservation_id < current_node.reservation_id:
                return self._find(current_node.left, reservation_id)
            else:
                return self._find(current_node.right, reservation_id)
        else:
            # jeśli node nie istnieje to
            return None


    def delete(self, reservation_id: int):
        self.root = self._delete(self.root, reservation_id)
        return reservation_id

    def _delete(self, current_node: Node, reservation_id: int):
        if current_node is None:
            return current_node
        
        if reservation_id < current_node.reservation_id:
            current_node.left = self._delete(current_node.left, reservation_id)
        elif reservation_id > current_node.reservation_id:
            current_node.right = self._delete(current_node.right, reservation_id)
        else:
            # usuwanie
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            # jeśli węzeł ma 2 dzieci, znajdź najmniejszy węzeł w prawym węźle
            temp = self.find_min(current_node.right)

            # skopiowanie węzła do aktualnego węzła
            current_node.reservation_id = temp.reservation_id
            current_node.passenger_name = temp.passenger_name
            current_node.flight_date = temp.flight_date

            # usunięcie najmniejszego węzła z prawego węzła
            current_node.right = self._delete(current_node.right, temp.reservation_id)
        return current_node




    def find_min(self, current_node: Node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node





#=======================================================

# Wywołanie klasy
bst = BinarySearchTree()

# Dodanie rezerwacji
bst.insert(100, "John Dee", "2023-10-05")
bst.insert(101, "Jane Dee", "2023-10-05")
bst.insert(99, "Alice Dee", "2023-10-05")

# Wyszukanie rezerwacji
found = bst.find(100)
if found:
    print(f"Znaleziono rezerwację: {found.passenger_name} z dnia {found.flight_date}.")
else:
    print("Rezerwacja nie znaleziona.")

# Anulowanie rezerwacji
cancel = bst.delete(100)
print(f"Anulowano rezerwację {cancel}")