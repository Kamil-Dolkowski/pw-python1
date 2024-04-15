# Autentykacja i autoryzacja użytkowników, zarządzanie uprawnieniami i rolami, zabezpieczenia przed SQL Injection w MSSQL Server

#-----------------------------------------------------------------------------------------

# Znaczenie bezpieczeństwa informacji:
-kluczowe aspekty: poufność, integralność, dostępność danych
-ryzyka i zagrożenia: naruszenia danych, wyciek poufnych informacji, utrata danych, ataki typu SQL Injection
-skutki naruszeń bezpieczeństwa: straty finansowe, szkody reputacyjne, konsekwencje prawne
-przykład z życia: naruszenie danych w dużej firmie, pokazujące potencjalne skutki braku odpowiednich zabezpieczeń

#-----------------------------------------------------------------------------------------

"SELECT * FROM DB WHERE id = 10";
                            "+zmienna+"
                            zmienna = '"; DROPTABLE;"';


#--------------------

WHERE id=10             <- wyświetli tylko id=10
WHERE id=10 or 1=1      <- wyświetli wszystko

#-----------------------------------------------------------------------------------------

# Podstawowe komponenty bezpieczeństwa:
-autentykacja i autoryzacja (autentykacja Windows i SQL; role i uprawnienia do zarządzania dostępem)
-szyfrowanie (TDE - Transparent Data encryption; szyfrowanie połączeń (SSL/TLS) )
-zarządzanie audytem i monitorowanie
-zabezpieczenie przed SQL Injection (stosowanie parametryzowanych zapytań i minimalizacja uprawnień)

#-----------------------------------------------------------------------------------------

Definicja bezpieczeństwa bazy danych - ochrona danych przed nieautoryzowanym dostępem, zniszczeniem lub modyfikacją

#-----------------------------------------------------------------------------------------

# SQL Injection

SQL Injection - wstrzykiwanie złośliwych instrukcji SQL do zapytać -> nieautoryzowany dotęp do danych

Jak się przed tym bronić?:
-parametryzowane zapytania
-walidacja i sanitacja danych wejściowych
-minimalizacja uprawnień użytkowników bazy danych

#-----------------------------------------------------------------------------------------

# Wyciek danych

Przyczyny wycieków danych:
-ataki hakerskie
-błędy konfiguracji systemu
-niewłaściwe zarządzanie uprawnieniami dostepu

Metody ochrony:
-szyfrowanie danych w spoczynku i transmisji
-regularne przeglądy i aktualizacje polityk bezpieczeństwa
-audyty bezpieczeństwa i testy penetracyjne

#-----------------------------------------------------------------------------------------

# Naruszenie integralności danych

Ryzyka:
-błędne decyzje biznesowe
-utrata zaufania klientów

??

#-----------------------------------------------------------------------------------------

# Best practise:
-Aktualizacje i łatki bezpieczeństwa - regularne aktualizowanie serwera bazy danych oraz aplikacji korzystających z bazy
-minimalizacja uprawnień - nadawanie użytkownikom i aplikacjom tylko niezbędnych uprawnień
-szyfrowanie i zarządznie kluczami - szyfrowanie połączeń i danych wrażliwych, zarządzanie kluczmi szyfrowania
-regularne audyty i monitorowanie

#-----------------------------------------------------------------------------------------

# Autentykacja użytkowników

2 główne tryby uwierzytelniania:
-uwierzytelnianie Windows ?
- ?

#---------------------------------------

# uwierzytelnianie Windows

uwierzytelnianie Windows - używa kont Windows do uwierzytelniania uzytkowników, wykorzytuje mechanizmy zabezpieczeń Windows, 
by zarzadzać identyfikacją użytkowników i autoryzacją dostępu do bazy danych

Zalety:
-bezpieczeństwo - silne mechanizmy zabezpieczeń Windows
-zarządzanie - centralne zarządzanie kontami i politykami bezpieczeństwa przez Active Directory
-mniej hasła - 1 hasło

kiedy uzywać? -> środowiska korporacyjne z centralnym zarządzaniem użytkownikami i zasobami

#---------------------------------------

# uwierzytelnianie SQL Server

uwierzytelnianie SQL Server - nazwy użytkowników i haseł zarządzane przez SQL Server, nie zależy od kont systemu operacyjnego

Zalety:
-elastyczność - możliwość dostępu z systemów niezintegrowanych z Windows
-niezależność - nie wymaga kont Windows ani dostępu do Active Directory

kiedy uzywać? -> rozproszone lub heterogeniczne środowiska, gdzie nie wszystkie systemy klientów są zintegrowane z Active Directory

Zalety:
-obsługa starszych aplikacji
-środowiska z mieszanymi stystemami operacyjnymi
-obsługa aplikacji internetowych

Wady:
-wiele loginów i haseł
-nie może korzystać z protokołu bezpieczeństwa Kerberos
-Windows oferuje dodatkowe zasady dotyczące haseł , które nie są dostępne dla logowania SQL Server

#-----------------------------------------------------------------------------------------

Przejście z uwierzytelniania Windows na uwierzytelnianie SQL Server:



**
Security -> Logins -> sa -> properties

**
SQL Server Configuration Manager -> SQL Server Services -> SQL Server -> restart

#-----------------------------------------------------------------------------------------

# Authentication / Uwierzytelnienie

potwierdzenie tożsamości:
-login
-hasło

Jak się zabezpieczyć?:
-hashowanie haseł (jednokierunkowy proces, który przekształca dane wejściowe w ciąg o stałej długości)
-szyfrowanie danych
-używanie bezpiecznych połączeń (np. HTTPS, by uniknąć przechwycenia przez nieautoryzowane osoby)

#-----------------------------------------------------------------------------------------

Autoryzacja:
# Uprawnienia Server/Database

GRANT SELECT ON SCHEMA::HumanResources TO role_HumanResourcesDept;      (nadawanie uprawnień)
REVOKE SELECT ON SCHEMA::HumanResources TO role_HumanResourcesDept;     (zmienianie uprawnień ?)

GRANT - nadaje uprawnienia
REVOKE - usuwa uprawnienia, nie blokuje możliwości ponownego przyznania
DENY - aktywnie blokuje uprawnienia , ma wyższy priorytet niż GRANT

#-----------------------------------------------------------------------------------------

# Wpływ na dziedziczone i eksplikowane ??
-dziedziczone uprawnienia
-eksplikowane uprawnienia

#-----------------------------------------------------------------------------------------

# Uprawnienia na poziomie serwera

CREATE LOGIN
-tworzenie nowych logowań do serwera
CREATE LOGIN MyLogin WITH PASSWORD='strongpassword';


VIEW SERVER STATE
-wyświetlanie ogólnego stanu serwera
SELECT * FROM sys.dm_os_performance_counters;


ALTER SERVER ROLE
-modyfikowanie ról serwera
ALTER SERVER ROLE sysadmin ADD MEMBER MyLogin;


Inne:
CONTROL SERVER - pełna kontrola nad serwerem (UWAGA!)
ALTER ANY LOGIN - modyfikacja dowolnego logowania na serwerze
VIEW ANY DEFINITION - wyświetlanie definicji wszystkich obiektów na serwerze

#-----------------------------------------------------------------------------------------

Linked Servers - podlinkowane serwery

#-----------------------------------------------------------------------------------------

# Best Practise:
-zasada minimalnych uprawnień
-regularne przeglądy uprawnień
-monitorowanie i audytowanie

#-----------------------------------------------------------------------------------------

Uprawnienia na poziomie bazy danych

#-----------------------------------------------------------------------------------------

# Role na poziomie bazy danych:
-db_owner - pełne uprawnienia
-db_datareader - czytanie ...
-db_datawriter
-db_ddladmin
-db_securityadmin

292 uprawnienia w MSSQL

#-----------------------------------------------------------------------------------------

# Tworzenie włsanych ról

CREATE ROLE
GRANT, DENY, REVOTE

#-----------------------------------------------------------------------------------------

# Schematy
Schematy - kluczowa warstwa abstrakcji, umożliwia grupowanie obiektów (tabele, widoki, itp.)
organizacja obiektów, zarządzanie uprawnieniami na poziomie grupy obiektów


Schemat - kontener nazw dla obiektów bazy danych
(przestrzeń nazw)

Korzyści:
-lepsza organizacja
-bezpieczeństwo
-elastyczność

#-----------------------------------------------------------------------------------------

# Zarządzanie uprawnieniami za pomocą schematów

centralne zarządzanie uprawnieniami dla grupy obiektów

#---------------------------------------ZADANIA-------------------------------------------

# 1. Tworzenie użytkownika: (NowyPracownik bez logowania)

CREATE USER NowyPracownik WITHOUT LOGIN;

# 2. Przyznanie roli: (db_datareader dla NowyPracownik)

ALTER ROLE db_datareader ADD MEMBER NowyPracownik;

# 3. Zarządzanie uprawnieniami: (instrukcja SELECT na tabeli HumanResources.Employee dla NowyPracownik)

GRANT SELECT ON HumanResources.Employee TO NowyPracownik;

# 4. Tworzenie własnej roli: (HR_Manager - zarządzanie danymi w schemacie HumanResources)
                             (HR_Manager uprawnienia do SELECT, INSERT, UPDATE, DELETE na wszystkich tabelach w schemacie HumanResources)

CREATE ROLE HR_Manager;

GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::HumanResources TO HR_Manager;

# 5. Przyznanie roli użytkownikowi: (NowyPracownik -> HR_Manager)

ALTER ROLE HR_Manager ADD MEMBER NowyPracownik;


#-----------------------------------------------------------------------------------------

Revert;
use AdventureWorks2019
-- 1

CREATE USER NowyPracownik WITHOUT LOGIN;

GO

-- 2

ALTER ROLE db_datareader ADD MEMBER NowyPracownik;

GO

-- 3

GRANT SELECT ON HumanResources.Employee TO NowyPracownik;

GO

-- 4

CREATE ROLE HR_Manager;

GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::HumanResources TO HR_Manager;

GO

-- 5

ALTER ROLE HR_Manager ADD MEMBER NowyPracownik;

GO

#-----------------------------------------------------------------------------------------

