# Listy jednokierukowe i dwukierunkowe

# jednokierunkowa- wskazuje nastepny element, a ostatni wskazuje na None
# prosta implementacja
# efektywna w dodawaniu i usuwaniu elementow na poczatku listy

# dostep do elementow tylko w jednym kierunku
# trudnosc w usuwaniu ostatniego elementu
# zastosowanie: w kolejkach, stosach, historii przegladania w przegladarkach

#LISTA JEDNOKIERUNKOWA
class Node:
    def __init__(self,data):
        self.data = data #przechowywanie danych elementu
        self.next=None #wskażnik na nastepny element

class SinglyLinkedList:
    def __init__(self) :
        self.head=None #głowa listy, poczatkowo none
    def append(self,data):
        #dodawanie elementu na koniec listy
        if not self.head:
            self.head=Node(data) #jesli lista jest pusta, nowy element staje sie head
            return
        last=self.head
        while last.next:
            last=last.next #przechodzenie do ostatniego elementu
        last.next=Node(data) #tworzenie nowego elementu na koncu
    def display_all(self):
        #wyswietlenie wszystkich wartosci wraz z nastepna wartoscia
        current=self.head
        while current:
            next_value= current.next.data if current.next else "None"
            print(f"{current.data}, Next: {next_value}")
            current=current.next
        
    def display(self,data):
        #wyswietlenie pojedynczej wartosci wraz z nastepna wartoscia
        current=self.head
        while current:
            if current.data ==data:
                next_value= current.next.data if current.next else "None"
                print(f"{current.data}, Next={next_value}")
                return
            current=current.next
        print("Wartosc nie istnieje")
              

# lista= SinglyLinkedList()
# lista.append(1)
# lista.append(2)
# lista.append(3)
# lista.display_all()
# lista.display(2)





# LISTA DWUKIERUNKOWA
#  to samo co lista dwukierunkowa, tylko wskazuje do poprzedniej i nastepnej wartosci
# ZALETY
# nawigacja w obie strony
# latwiejsze usuwanie danych
# WADY
# wieksze uzycie pamieci
# skomplikowana implementacja w porownianiu do jednokierunkowych
# ZASTOSOWANIE:
# kolejka priorytetowa
# zarzadzania zakladnkami w przegladarkach

class NodeTwo:
    def __init__(self,data):
        self.data = data #przechowywanie danych elementu
        self.next=None #wskażnik na nastepny element
        self.previous=None #wskaznik na poprzedni
        
class TwoLinkedList:
    def __init__(self) :
        self.head=None #głowa listy, poczatkowo none
    def append(self,data):
        #dodawanie elementu na koniec listy
        if not self.head:
            self.head=NodeTwo(data) #jesli lista jest pusta, nowy element staje sie head
            return
        last=self.head
        while last.next:
            last=last.next #przechodzenie do ostatniego elementu

        new=NodeTwo(data)
        last.next=new #tworzenie nowego elementu na koncu
        new.previous=last
    def display_all(self):
        #wyswietlenei wszystkich wartosci wraz z nastepna wartoscia
        print("\nDisplay all value:")
        current=self.head
        while current:
            previous= current.previous.data if current.previous else "None"
            next_value= current.next.data if current.next else "None"
            print(f"Value: {current.data}, Next: {next_value}, Previous: {previous}")
            current=current.next
        
    def display(self,data):
        #wyswietlenei  wartosci wraz z nastepna wartoscia i poprzednia wartoscia, dla podanej w wejsciu wartosci
        print(f"\nDisplay one value {data}:")
        current=self.head
        while current:
            if current.data ==data:
                next_value= current.next.data if current.next else "None"
                previous= current.previous.data if current.previous else "None"
                print(f"Value: {current.data}, Next={next_value}, Previous: {previous}")
                return
            current=current.next
        print("Wartosc nie istnieje")
        
        
# lista2= TwoLinkedList()
# lista2.append(1)
# lista2.append(2)
# lista2.append(3)
# lista2.display_all()
# lista2.display(1)




# # Tablice samorozszerzające
# list() - lista zachowuje sie jako tablica samorozszerzająca, umozliwia dynamiczne dodawanie i usuwanie elementów bez koniecznosci recznego alokowania pamieci
# listy moga zawierac wartosci roznych typow i automatycznie dostosuwuja swoj rozmiar
# dzialaja tak ze alokuja dodatkowa pamiec gdy rozmiar przekoczy jej aktualna pojemnosc
# # gdy tak jest to python alokuje nowa wieksza tablice i kopiuje a stara liste usuwa
# zalety: elastycznosc,prostota,wydajnosc
# wady: koszt kopiowania, nieprzewidywania wydajnosc
# moja_lista=[]
# moja_lista.append("fd")
# moja_lista.append("fdddd")
# print(moja_lista)
# moja_lista.remove("fddddddd")
# print(moja_lista)

# #symulacja obslugi kolejki osob oczekujacych na zakup biletów w kinie
# dodanie osoby do konca kolejki
# obsluzenie osoby z przodu kolejki i usuniecie jej z kolejki
# wyswietlenie stanu kolejki
# dodawanie grupy do kolejki
# usuwanie okreslonej osoby na podstawie imienia


class Kolejka:
    def __init__(self):
        self.kolejka= []
        
    def dodaj_na_koniec(self,person):
        kolejka=self.kolejka
        kolejka.append(person)
        print(f"dodano {person} do kolejki")
        
    def obsluz(self):
        kolejka=self.kolejka
        kolejka.pop(0)
        print("obsluzono osobe")
        
    def pokaz(self):
        kolejka=self.kolejka
        print("KOLEJKA:")
        for i in range(len(kolejka)):
            print(f"{i}. {kolejka[i]}")
        
    def dodaj_grupe(self,grupa):
        kolejka=self.kolejka
        kolejka.extend(grupa)
        
    def usun_z_kolejki(self,person):
        try:
            kolejka=self.kolejka
            kolejka.remove(person)
            print(f"usunieto {person} z kolejki")
        except ValueError: print("Nie ma takiej osoby")
        
# kolejka=Kolejka()
# kolejka.dodaj_na_koniec("ala")
# kolejka.dodaj_na_koniec("adam")
# kolejka.dodaj_na_koniec("pawel")
# kolejka.pokaz()
# kolejka.usun_z_kolejki("ala")
# kolejka.pokaz()




# PROCENT SKŁADANY
# funkcja do oblicznania przyszlej wartosci inwestycji z wykorzystaniem procentu skladanego

# parametry:
#     p(float): poczatkowa kwota inwestycji
#     f(float): roczna stopa procentowa w formie dzisietnej
#     n(int): liczba okresow kapitalizacji rocznie
#     t(float)L czas trwania inwestycji w latach
    
#     zwraca float: przyszla wartosc inwestycji

# p * (1+f)^n =koniec

p=10000
r=0.03
n=3
t=3

def procent_skladany(p,r,n,t):
    kapital=p
    p = p * (1+r)**t
    kwota_koncowa=round(p,2)
    zysk=kwota_koncowa-kapital
    print(f"Czas trwania: {t} lata, Oprocentowanie: {r},Kapitał: {kapital}, Kwota końcowa: {kwota_koncowa}, Zysk: {round(zysk,2)}") 

procent=procent_skladany(p,r,n,t)

# coś źle ^