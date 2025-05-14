# Baza

### Pacjent 
* id
* imię
* nazwisko
* imie2
* wiek

### Wizyta
* id
* pacjent_id
* lekarz_id
* opis
* zalecenia

### Recepta
* id
* wizyta_id

### Produkt
* id
* recepta_id
* nazwa

### Skierowanie
* id
* wizyta_id

### Badanie
* id
* skierowanie_id

### Lekarz
* id
* imię
* nazwisko
* imie2

# Uwagi

Pomiędzy recepta a produkt jeszcze jedna tabela łącząca

* zadania zrobić na maszynie wirtualnej
* wyniki zadań w formie sprawozdania

# Zadania

## 1. Porównanie zapisu i wydobywania danych z obciążonego postgresql-a (dużo danych, równoległe zapytania z wielu procesów)

* 1 milion pacjentów, średnio 5/10 wizyt na 1 pacjenta
* 5 milionów wizyt
* na co 2 wizycie pacjent powinien dostać skierowanie i receptę
* testy dla różnych rozmiarów bazy (czy zależność jest liniowa?)
* ile zajmuje zapis? (czy prędkość się zmienia wraz z rozmiarem bazy)
* równocześnie update i select

## 2. Ile miejsca zajmuje missing value/null?

* najpierw wypełnić bazę danymi w 100% -> ile zajmuje miejsca na dysku?
* potem generujemy dokładnie taką samą bazę, w której null-e zajmują 10%, 20%, ..., 100% -> ile zajmuje miejsca na dysku?
* w tabelach kolumny różnego typu (text, varchar(64), varchar(256), timestamp, int, blob (pole binarne) [rentgen] [30MB])

## 3. Porównanie hd5, parquet, avro

* różnice w prędkości zapisu, odczytu
* czy można odczytywać dane selektywnie? (np. linia 5)
* jak wygląda modyfikacja danych (czy można coś dopisywać, jaki koszt, ile zajmuje taka operacja)
* czy jest możliwy update i jak on wygląda

## 4. Hadoop, hdfs and save data i 1B, 1KiB, 10KiB, ...

* hdfs - rozproszony system plików
* zapewnia bezpieczeństwo, część danych to duplikaty
* system dla dużych plików, nie dla małych
* 100MB - alokacja pamięci
* nie nadaje się do składowanie małych plików
* jak się zachowuje, kiedy zapiszemy 1B, 1KiB, 10KiB, ...
* ile te dane skonsumowały miejsca?

## 5. Dystrybucja plików w katalogach [praca solo]

* utworzyć katalog z dużą liczbą plików (każdy po 1MB) (100-200? tysięcy plików)
* czy ma znaczenie rozmieszczenie tych plików?
* najpierw wszystkie pliki w 1 katalogu, potem rozdzielenie na kilka katalogów
* ile każdemu procesowi zajmuje odczytanie plików?
* czy spadek wydajności jeśli pliki są w 1 katalogu

## 6. Janus db

* baza grafowa
* zainstalować i spróbować z poziomu jakiegoś języka dodać, usunąć, pobrać dane
* można oprzeć na przykładzie medycznym

## 7. Apache ignite

* baza klucz-wartość
* baza in memory
* zainstalowanie i seria przykładów jak to użyć (select, insert, update)
* można oprzeć na przykładzie medycznym
* pod jednym kluczem są informacje o pacjencie, jego ostatnich wizytach i wydanych receptach
* krótki opis, wprowadzenie, do czego te bazy są wykorzystywane

## 8. Algorytm genetyczny

* rozwiązanie problemu jako ciąg 0-1
* np. poszukiwanie minimum pewnej funkcji
* populacja - zbiór ciągów (każdy to 1 możliwe rozwiązanie)

```
                    funkcja przystosowania
                               |
                              \|/
            /  1011010100 --> f(x)
populacja  |   1110001010 --> f(x)
            \  0001100100 --> f(x)
```

* z tej populacji wygenerować nową populację i ponowić proces
* populacje powyżej 1000

* poszukiwanie minimum pewnej funkcji
* wykorzystać procesy
* operacja krzyżowania - wybieram losowo, ale te lepsze mają większe szanse
* wybieram 2 ciągi

A - B
1 - 2

po zmianie:

A - 2
1 - B

## 9. Aplikacja webowa (fastAPI lub Flask) + Firebase

* składowanie 'json' w bazie Firebase
* aplikacja webowa, która zapisuje dane o pacjentach do Firebase
* (*) Dla chętnych + aplikacja mobilna wyciągająca dane

&nbsp;

# Wybrane projekty 

## 1. Porównanie zapisu i wydobywania danych z obciążonego postgresql-a (dużo danych, równoległe zapytania z wielu procesów)

* 1 milion pacjentów, średnio 5/10 wizyt na 1 pacjenta
* 5 milionów wizyt
* na co 2 wizycie pacjent powinien dostać skierowanie i receptę
* testy dla różnych rozmiarów bazy (czy zależność jest liniowa?)
* ile zajmuje zapis? (czy prędkość się zmienia wraz z rozmiarem bazy)
* równocześnie update i select

## 5. Dystrybucja plików w katalogach [praca solo]

* utworzyć katalog z dużą liczbą plików (każdy po 1MB) (100-200? tysięcy plików)
* czy ma znaczenie rozmieszczenie tych plików?
* najpierw wszystkie pliki w 1 katalogu, potem rozdzielenie na kilka katalogów
* ile każdemu procesowi zajmuje odczytanie plików?
* czy spadek wydajności jeśli pliki są w 1 katalogu

## 7. Apache ignite

* baza klucz-wartość
* baza in memory
* zainstalowanie i seria przykładów jak to użyć (select, insert, update)
* można oprzeć na przykładzie medycznym
* pod jednym kluczem są informacje o pacjencie, jego ostatnich wizytach i wydanych receptach
* krótki opis, wprowadzenie, do czego te bazy są wykorzystywane