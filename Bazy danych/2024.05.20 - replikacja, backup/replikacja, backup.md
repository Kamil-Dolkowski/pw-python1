# Replikacja i backup danych

#-------------------------------------REPLIKACJA------------------------------------------

# Replikacja
-to proces kopiowania i utrzymywania danych oraz obiektów bazodanowych w wielu bazach danych w celu poprawy dostępności, skalowalności i wydajności
-umożliwia synchronizację danych pomiędy różnymi serwerami i lokalizacjami 

SELECT'y nie powinny być w transakcjach !

#-----------------------------------------------------------------

# Typy replikacji:
# -replikacja transakcyjna:
-propaguje zmiany danych z bazy publikacji do baz subskrybentów w sposób ciągły, niemal w czasie rzeczywistym
-Zastosowanie: idealna dla środowisk, gdzie nie ważna jest minimalna latencja w synchronizacji danych
-Proces:
    -wstępne załadowanie danych z migawki (snapshot)
    -ciągłe przesyłanie zmian danych (wstawianie, aktualizowanie, usuwanie)
# -replikacji migawkowa:
-tworzy pełną kopię danych w określonych odstępach czasu
-przydatna dla aplikacji, gdzie aktualizacje danych są rzadkie i mniej istotna jest natychmiastowa konsystencja
# -replikacja mieszana:
-łączy cechy replikacji transakcyjnej i migawkowej, (bardziej elastyczne)
-Zastosowanie: różna częstotliwość aktualizacji danych 



latencja - opóźnienie w synchronizacji danych lub w komunikacji

ransomware -> szyfrowanie, drop table
Git CICD
LDAP

#-----------------------------------------------------------------

# Możliwości i zastosowania replikacji:
-wysoka dostępność - dostęp do danych nawet w przypadku awarii serwera głównego
-skalowalność ! - rozłożenie obciążenia odczytu danych na wiele serwerów
-migracja danych - przenoszenie danych pomiędzy serwerami lub centrami danych bez postojów
-zapasowa kopia danych - kopie zapasowe w różnych lokalizacjach

#-----------------------------------------------------------------

# Replikacja transakcyjna:

Zalety:
-niska latencja
-konsystencja danych niem la w czasie rzeczuywistym

Wady:
-złożoność konfiguracji
-większe wymagania dotyczące zasobów

# Replikacji migawkowa:

Zalety:
-prosta konfiguracja
-mniejsze wymagania dot zasobów

Wady:
-dane mogą być przestarzałe między migawkami
-niska częstotliwość aktualizacji

#-----------------------------------------------------------------

CREATE DATABASE PublikacjaDB;


EXEC sp_replicationdboption
    @dbname = 
    @optname = 
    @value = 


EXEC sp_addistributor
    @distributor = 'NazwaSerwera',
    @password = 'haslo';

#---------------------------------------BACKUP--------------------------------------------

# Backup
-proces tworzenia kopii danych, które mogą być użyte do przywrócenia oryginału po utracie danych

Odzyskiwanie odnosi się do procesu przywracania tych kopii do pierwotnej lokalizacji w przypadku awarii.
-bezopieczeństwo danych
-minimalizacja czasu przestoju i utraty danych 
-spełnienie wymagań prawnych i biznesowych

NazwaBazy -> Tasks -> Back Up...

#-----------------------------------------------------------------

# Rodzaje backupów:
# -backup pełny:
    -kompletna kopia bazy danych
    -podstawa innych typów backupów
    -Zalety: pełna kopia wszystkich danych
    -Wady: duży rozmiar i długi czas tworzenia
# -backup różnicowy:
    -zawiera tylko zmiany dokonane od ostatniego backupu pełnego
    -redukcja czasu i rozmiaru backupu
    -Zalety: mniejsze i szybsze w porównaniu do backupu pełnego
    -Wady: wymaga ostatniego backupu pełnego do przywrócenia danych
# -backup dziennika transakcji:
    -kopiuje wszytskie transakcje dokonane od ostatniego backupu dziennika
    -
    -Zalety: minimalizuje utratę danych
    -Wady: wymaga sekwencji ...

#-----------------------------------------------------------------

# Strategie backupu:
# -Strategia kopii zapasowych:
-plan tworzenia backupów w celu zapewnienia integralności i dostępności danych
-Elementy:
    -backupy pełne co tydzień
    -backupy różnicowe codziennie
    -backupy dziennika transakcji co godzinę
# -Okresy retencji:
-czas, przez który backupy są przechowywane przed ich usunięciem
-Przykład:
    -backupy pełne: 1 miesiąc
    -backupy różnicowe: 2 tygodnie
    -backupy dziennika transakcji: 1 tydzień
# -Harmonogramy backupów:
-regularne wykonywanie backupów zgodnie z ustalonym planem
-Przykład:
    -backupy pełne: każda niedziela o 2:00
    -backupy różnicowe: codziennie o 20:00
    -backupy dziennika transakcji: co godzinę

#-----------------------------------------------------------------

# Disaster Recovery (DR) 
-proces odzyskiwania danych i przywracania funkcjonalności systemów po awarii

# Wskaźniki RTO i RPO:
-RTO (Recovery Time Objective) - maksymalny akceptowalny czas, w którym systemy muszą zostać przywrócone po awarii
-RPO (Recovery Point Objective) - maksymalna ilość danych, które mogą zostać utracone mierzone w czasie


Controller Write

#-----------------------------------------------------------------

# Backup pełny

BACKUP DATABASE NazwaBazyDanych
TO DISK = 'C:\Backup\NazwaBazyDanych_Full.bak'
WITH FORMAT, MEDIANAME = 'SQLServerBackups',
NAME = 'Pełny Backup NazwaBazyDanych';


# Backup różnicowy  

(???)

BACKUP DATABASE NazwaBazyDanych
TO DISK = 'C:\Backup\NazwaBazyDanych_Full.bak'
WITH DIFFERENTIAL
WITH FORMAT, MEDIANAME = 'SQLServerBackups',
NAME = 'Pełny Backup NazwaBazyDanych';


# Odzyskiwanie danych

RESTORE DATABASE NazwaBazyDanych
FROM DISK = 'C:\Backup\NazwaBazyDanych_Full.bak',
WITH NORECOVERY;


# Odzyskiwanie logów

RESTORE LOG NazwaBazyDanych
FROM DISK = 'C:\Backup\NazwaBazyDanych_Logs.bak',
WITH RECOVERY;

#-----------------------------------------------------------------

-regularne wykonywanie backupów dla zapewnienia bezpieczeństwa
-wybór odpowiedniej strategii backupu i DR zależy od specyficznych wymagań biznesowych
-monitorowanie i testowanie procedur backupu i odzyskiwania danych jest niezbędne dla ich skuteczności


# Najlepsze praktyki:
-regularnie testuj proces odzyskiwania danych
-przechowuj ??


# zasada 3-2-1:
3 backupy: 2 w tej samej lokalizacji, 1 w innej

#-----------------------------------------------------------------

# Tabele w msdb:

-backupset
  -zawiera informacje o każdym wykonanym backupie

-backupmediafamily
  -zawiera informacje o mediach backupowych, na których są przechowywane backupy

-backupfile
  -informacje o plikach wchodzących w skład backupu

#-----------------------------------------------------------------

# Widoki w msdb:

-backupfilegroup
  -zawiera informajce o grupach plików ?/

-backupmediafamily

-backupset

#-----------------------------------------------------------------

# Procedury systemowe w msdb:

#sp_backupdatabase

-sp_add????

-sp_delete_backuphistory
  -usuwa przestarzałe wpisy historii backupów

