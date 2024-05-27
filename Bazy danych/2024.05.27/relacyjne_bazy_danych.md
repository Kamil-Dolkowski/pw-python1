# NoSQL i relacyjne bazy danych

#----------------------------------------------------------------

# Relacyjne bazy danych (RDBMS)
-dane w wierszach i kolumnach
-tabele mają określony schemat

# Cechy:
-struktura tabelaryczne
-schematy danych 
-ACID dla spójności transakcji
-język SQL

# Przykłady:
-MySQL
-PostgreSQL
-Oracle Database
-Microsoft SQL Server

#- - - - - - - - - - - - - - - - 

# NoSQL (Not Only SQL)
-bardziej elastyczne
-łatwe skalowanie i elastyczne zarządznie różnorodnymi typami danych
-dane przechowywane w sposób niestrukturalizowany

# Cechy:
-elastyczna struktura danych
-skalowalność pozioma
-BASE dla spójności danych
-różnorodne modele przechowywania danych

# Przykłady:
-MongoDB (dokumentowe)
-Cassandra (szerokie kolumny)
-Redis (klucz-wartość)
-Neo4j (grafowe)
-CouchDB (dokumentowe)
-Amazon DynamoDB (klucz-wartość)

#----------------------------------------------------------------

# Historia relacyjnych baz danych
lata 70. XX wieku
-1970 - artykuł Edgara F. Codda (pracownika IBM) z koncepcją relacyjnych baz danych
-1974 - prototypowa implementacja relacyjnej bazy danych stworzona przez IBM

lata 90. XX w.
-1995 - powstanie MySQL
-1996 - premiera PostGresa

# Historia baz danych NoSQL
koniec lat 90. XX w.
-1998 - powstanie pierwszej bazy
-2000

-2007 - wydanie CouchDB
-2008 - powstanie Apache Cassandra przez Facebooka
-2009 - premiera MongoDB
-2010 - powstaje termin "NoSQL"
-2010 - Apache HBase wydana jako część ekosystemu Apache Hadoop
-2011 - Redis zyskuje popularność

#----------------------------------------------------------------

# Struktura danych
-tabele
-wiersze
-kolumny


-Dokumenty:

{
    "id": 1,
    "name": "Jan",
    "birthdate": "1990-01-01:,
    "address": {
        "street": "Kwiatka 1
        ...
    }
}


-Grafy:

(Jan)-[Przyjaciel]  ....??


-Klucz-wartość


-Szerokie kolumny

Row 1: {"ID": 1, "Imie": "Jan", "Nazwisko": "Kowalski"}
Row 2: {"ID": 1, "Imie": "Jan", "Nazwisko": "Kowalski", "Miasto": "Kraków"}

#----------------------------------------------------------------

# Bazy relacyjne

# Zalety
-niezawodność
-spójność danych (ACID)
-złożone zapytanie (SQL) - skomplikowane operacje na danych, np. JOIN, GROUP BY

# Wady:
-mniejsza skalowalność 
-sztywność schematów
-koszty utrzymania (koszty licencji i konserwacji)

#- - - - - - - - - - - - - - - - 

# NoSQL

# Zalety
-elastyczność
-skalowalność (pozioma)
-szybkie operacje na dużych zbiorach danych (analiza w czasie rzeczywistym, big data, aplikacje internetowe)

# Wady:
-mniejsza spójność (BASE)
-brak standaryzowanych języków zapytania
-trudniejsze zarządzanie złożonymi transakcjami

#----------------------------------------------------------------

# Przykład 1: Facebook

Przechowywanie i analiza ogromnych ilości danych
-codzienne generowanie ogromnej ilości z postów, zdjęć ,komentarzy

Apache Cassandra
-rozproszona baza danych NoSQL

Dlaczego?:
-wysoka skalowalność
-niskie opóźnienia
-dodatkowe korzyści (rozproszona architektura - wysoka dostępność i odporność na awarie)

#- - - - - - - - - - - - - - - - 

# Przykład 2: Bankowość

Wysoka spójność i niezawodność transakcji

Oracle Database

Dlaczego?:
-zgodność z ACID
-bezpieczeństwo danych (szyfrowanie danych, kontrola dostępu, audyty)
-dodatkowe korzyści (wysoka dostępność i niezawodnośc, kopie zapasowe i odzyskiwanie danych, skalowenie w pionie)

#----------------------------------------------------------------

# Kiedy relacyjne bazy danych?:
-transakcje finansowe
-systemy zarządzania danymi
-aplikacje wymagające złożonych zapytań i analiz

# Kiedy bazy NoSQL?:
-aplikacje internetowe o dużej skali (e-commerce, social media)
-systemy analityczne i big data
-aplikacje z dynamicznie zmieniającymi się schematami danych

#----------------------------------------------------------------

# Koszty infrastruktury

Serwery i skalowalność:
-Relacyjne bazy danych:
    -serwery: wysokie wymagania dotyczące sprzętu
    -skalowalność: pionowa skalowalność jest kosztowna i ograniczona fizycznie
-NoSQL:
    -serwery: możliwość użycia tańszego sprzętu
    -skalowalnośc: pozioma skalowalność jest bardziej efektywna kosztowo

Koszty licencji i wsparcia
-Relacyjne bazy danych:
    -licencje: wysokie koszty licencji dla mokercyjnych systemów 
    -wsparcie: kosztowne umowy wsparcia
-NoSQL:
    ??
    ??

Koszty operacyjne:
-Relacyjne bazy danych:
    -zarządznie: specjalistyczna wiedza i doświadczenie
    -konserwacja: regularne aktualizacje, optymalizacje
-NoSQL:
    -zarządznie: mniej specjalistyczna wiedza (choć czasem też jest potrzebna specjalistyczna)
    -konserwacja: mniejsza częstotliwość i koszt konserwacji

#----------------------------------------------------------------

# Bezpieczeństwo danych:
-kontrola dostępu
    -Role-Based Access Control (RBAC) - zarządzanie dostępem użytkowników na podts. ich ról
    -granularne uprawnienia - definiowanie szczegółowych uprawnień na poziomie tabel, wierszy, kolumn
-szyfrowanie
    -szyfrowanie w spoczynku (at rest) i tranzycie (in transit)
    -Transparent Data Encryption (TDE)
-audyt i logowanie
    -pełne śledzenie aktywności użytkowników i operacji na danych
    -generowanie szczegółowych logów dostępu i zmian w danych

#----------------------------------------------------------------

# Narzędzia i technologie

-MySQL Workbench:
    -opis:
        -graficzne narzędzie do zarządzania bazą danych MySQL
        -umożliwia projektowanie, rozwijanie i administrowanie bazą danych
    -kluczowe funkcje:
        -projektowanie diagramów ER (Entity-Relationship)
        -tworzenie, edytowanie i zarządzanie sche,atami i tabelami
        -wykonywanie zapytań SQL, optymalizacja, debugownaie
        -migracja baz danych i tworzenie kopii zapasowych

-pgAdmin:

-MongoDB Compass:
    -wizualizacja struktury dokumentówi kolekcji
    -tworzenie, edytowanie i usuwanie elementów
    -wykonywanie zapytań agregacyjnych i filtrowanie danych
    -analiza wydajności i monitorowanie operacji na bazie

-Cassandra OpsCenter:

#----------------------------------------------------------------

# Przyszłość baz danych

# Hybrydowe podejście: łączenie relacyjnych i NoSQL

-elastyczność i skalowalność NoSQL + spójność i złożone zapytania relacyjnych baz danych

Przykłady
-Polyglot Persistence
-NewSQL

Korzyści:
-elastyczność
-optymalizacja wydajności
-zgodność z regulacjami



# Nowe rozwiąznia:
-bazy NewSQL:
    -Google Spanner
    -CockroachDB
-sztuczna inteligencja i uczenie maszynowe


# Innowacje:
-Serverless Databases: bazy danych jako usługa (DBaaS)
    -Amazon Aurora Serverless, Google Firestore
-Blockchain Databases
    -BigchainDB, IBM Blockchain


# Korzyści:
-automatyzacja - redukacja kosztów i czasu, dzięki automatycznemu zarządzaniu i optymalizacji
-skalowalność i elastyczność
-bezpieczeństwo i integralność

#----------------------------------------------------------------

xml

xslt
