# Big Data i analiza danych

#---------------------------------------------------------------------------------

pliki płaskie (pliki z danymi) -> np.  .csv .xml

#---------------------------------------------------------------------------------

# Relacyjne nazy danych w ekosystemie Big Data
-spójność danych (integralność, ograniczenia)
-normalizacja (zapobiega dublowaniu danych i niezgodnościom)
-1 język -> SQL
-transakcyjność (ACID) (atomowość, spójność, izolacja, trwałość)
-stała struktura danych: tabele, wiersze, kolumny
    -tabela - pewien byt, np. klienci, produkty
    -wiersz - pojedynczy rekord
    -kolumna - atrybut tabeli, typ danych
-klucze główne, obce, indeksy
    -klucz główny - unikalny identyfikator, nie NULL, jednoznaczność
    -klucz obcy - łączenie tabel, relacje
    -indeksy - przyspieszenie wyszukiwania danych

#---------------------------------------------------------------------------------

# Big Data
-ogromne zbiory danych; zbyt duże, złożone i szybko zmieniające się, aby można było je przetwarzać tradycyjnymi narzędziami i technikami

# Charakterystyka: (4 główne aspekty znane jako 4V)
-volume (objętość) - ogromna ilość danych generowana codziennie przez różne źródła, np. media społ., IoT
-velocity (prędkość) - szybkość, z jaką dane są generowane, zbierane i przetwarzane
-variety (różnorodnośc) - różne typy danych, strukturalne, półstrukturalne i niestrukturalne, np. audio, wideo
-veracity (prawdziwość) - jakość i wiarygodność danych, które mogą być szumem, niekompletne lub błędne


**
przedziały danych, np. temperatura aktualizuje się co 0,5 'C

#---------------------------------------------------------------------------------

# Rola relacyjnych baz danych w ekosystemie Big Data:
-trwałe przechowywanie danych (kluczowe dla danych krytycznych dla biznesu)
-transakcyjność (ACID, spójnośc danych, niezawodnośc operacji)
-zapytania i analiza (zaawansowana analiza, łatwe przeszukiwanie dużych zbiorów danych)

#---------------------------------------------------------------------------------

# Integracja z narzędziami Big Data (Hadoop, Spark)
-Hadoop - przechowywanie i przetwarzanie dużych zbiorów danych w rozproszonym środowisku; Sqoop umożliwia transfer danych między Hadoop a relacyjnymi bazami danych
-Spark - Apache Spark - silnik do przetwarzania danych w pamięci, szybkie przetwarzanie dużych zbiorów danych; konektory JDBC wydajne przetwarzanie

#---------------------------------------------------------------------------------

# Relacyjne bazy danych jako Big Data ??:
-indeksowanie
-partycje
-replikacja
-kompresowanie danych

#---------------------------------------------------------------------------------

# SLQ Server w dużym przedsiębiorstwie:

ABC Corporation działa na całym świecie

# Centralne przechowywanie danych:
-SQL Server przechowywuje dane transakcyjen ze wszystkich sklepów
-baza w jednym miejscu

# Analiza i reportowanie:
-SQL Server Reporting Services (SSRS)
-Power BI zintegrowane z SGL Server

# Integracja z systemami CRM i ERP:
-wymiana danych między systemami
-integracja z CRM - lepsze zarządzanie relacjami z klientami
-integracja z ERP - efektywne zarządzanie zasobami przedsiębiorstwa

# Integracja z Hadoop:
-dane z mediów społecznościowych, logi serwerów

# Integracja z Apache Spark:
-przetwarzanie danych w czasie rzeczywistym
-integracja z SQL Server łączenie danych historycznych z danymi

# PolyBase:
-zapytania T-SQL
-brak ręcznego przenoszenia danych, co przyspiesza analizę

# Zwiększona efektywnośc operacyjna:
-centralizacja danych i integracja z różnymi systemami -> efektywne zarządzanie operacjami


#---------------------------------------------------------------------------------

# ETL [Extract (wydobycie), Transform (transformacja), Load (ładowanie)]

Extract               Transform               Load

Data source 1       Transformation
                ->      engine        ->     Target
Data source 2


# Extract: 
-wydobywanie danych z różnych źródeł, np. bazy danych, pliki, systemy ERP, CRM, API
# Transform: 
-dane są przekształcane i przgotowane do załadowania; może obejmować czyszczenie danych, filtrowanie, agregacja, wzbogacanie, konwersja dormatów
# Load: 
-przetworzone dnae są ładowane do docelowego systemu, np. do hurtowni dnaych, bazy danych, system analityczny


- - - - - - - - - 
04.06.2024


ETL w pracy !

# Znaczenie w procesie przetwarzania danych:
-integracja danych
-jakość danych
-zarządzanie dużymi wolumenami danych
-automatyzacja procesów
-wsparcie dla analiz biznesowych

#- - - - - - - - - - - - - - - - - - - - 

# Hurtownie danych
-firmy gromadzą dane z różnych systemów operacyjnych

# Migracja danych

# Integracja danych z chmurami
-kompleksowa analiza danych i raportowanie
-różne aplikacje SaaS 

# Analiza danych klientów
-różne kanały: strony internetowe, e-maile, ...
-wydobywa dane, transformuje i ...

#- - - - - - - - - - - - - - - - - - - - 

# Narzędzia ETL:
-SQL Server Integration Services (SSIS)
-


# Zalety: (ETL)
-integracja z SQL Server
-bogaty interfejs użytkownika
-duża funkcjonalność
-rozszerzalność

# Wady:
-ograniczona skalowalnośc
-koszt
-platforma Windows


Apache Nifi

#---------------------------------------------------------------------------------

# Data Science
interdyscyplinarna dziedzina, która łączy wiedzę z zakresu statystyki, informatyki oraz dziedzin biznesowych
procesy gromadzenia, przetwarzania, analizy oraz interpretacji dużych i złożonych zbiorów danych
wspieranie decyzji biznesowych, przewidywanie trendów, ...

# Kluczowe elementy:
-eksploracja danych
-modelowanie predykcyjne
-wizualizacja danych
-automatyzacja procesów

# Umiejętności:
-znajomość statystyki i matematyki - metody statystyczne, algebra liniowa, rachunek całkowy i różniczkowy
-programowanie - Python, SQL, R, Jupyter Notebook
-uczenie maszynowe
-analiza danych
-wizualizacja danych
-komunikacja

# Narzędzia:
-języki programowania: Python, SQL, R
-biblioteki analityczne i machine learning
-narzędzia do eksploracji danych
-platformy Big Data
-??


# Przykłady:
-Analiza sentymentu w mediach społ.
-Predykcja churnu klientów
    churn - powody rezygnacji z danej usługi lub produktu
-Rekomendacje produktów
-Analiza koszyka zakupowego
-Monitorowanie jakości powietrza

#---------------------------------------------------------------------------------

