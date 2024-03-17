CREATE DATABASE BibliotekaPW

USE BibliotekaPW;

CREATE TABLE Autor (
	AutorID int PRIMARY KEY IDENTITY(1,1),
	Imie varchar(15) NOT NULL,
	Nazwisko varchar(30) NOT NULL,
	Pseudonim varchar(30)
);

CREATE TABLE Wydawnictwo (
	WydawnictwoID int PRIMARY KEY IDENTITY(1,1),
	Nazwa varchar(30) NOT NULL,
	Status varchar(30) NOT NULL
);

CREATE TABLE Recenzja (
	RecenzjaID int PRIMARY KEY IDENTITY(1,1),
	Ocena int NOT NULL,
    Tresc varchar(300),
    Username varchar(30) NOT NULL,
    Ukryj bit,
);

CREATE TABLE Gatunek (
	GatunekID int PRIMARY KEY IDENTITY(1,1),
	Nazwa varchar(20) NOT NULL,
    Ukryj bit
);

CREATE TABLE Lokalizacja (
	LokalizacjaID int PRIMARY KEY IDENTITY(1,1),
	Miasto varchar(30) NOT NULL,
    Ulica varchar(30) NOT NULL,
    Numer int NOT NULL,
    KodPocztowy varchar(6) NOT NULL,
    Wojewodztwo varchar(19) NOT NULL,
);

CREATE TABLE Ksiazka (
    BookID int PRIMARY KEY IDENTITY(1,1),
    AutorID int NOT NULL,
    Tytul varchar(50) NOT NULL,
    GatunekID int,
    Opis varchar(300),
    RecenzjaID int,
    RokWydania int,
    WydawnictwoID int,
    Status varchar(15) NOT NULL,
	FOREIGN KEY (AutorID) REFERENCES Autor(AutorID),
    FOREIGN KEY (GatunekID) REFERENCES Gatunek(GatunekID),
    FOREIGN KEY (RecenzjaID) REFERENCES Recenzja(RecenzjaID),
    FOREIGN KEY (WydawnictwoID) REFERENCES Wydawnictwo(WydawnictwoID)
);

CREATE TABLE GodzinyOtwarcia (
	GodzinyOtwarciaID int PRIMARY KEY IDENTITY(1,1),
	DzienTygodnia varchar(12) NOT NULL,
    Godziny varchar(11) NOT NULL,
    Status varchar(9) NOT NULL
);

CREATE TABLE Biblioteka (
	BibliotekaID int PRIMARY KEY IDENTITY(1,1),
	Nazwa varchar(40) NOT NULL,
    LokalizacjaID int,
    GodzinyOtwarciaID int,
    FOREIGN KEY (LokalizacjaID) REFERENCES Lokalizacja(LokalizacjaID),
    FOREIGN KEY (GodzinyOtwarciaID) REFERENCES GodzinyOtwarcia(GodzinyOtwarciaID)
);

CREATE TABLE Egzemplarz (
	EgzemplarzID int PRIMARY KEY IDENTITY(1,1),
	BookID int NOT NULL,
    Status varchar(20) NOT NULL,
    BibliotekaID int NOT NULL,
    Zuzycie int,
    FOREIGN KEY (BookID) REFERENCES Ksiazka(BookID),
    FOREIGN KEY (BibliotekaID) REFERENCES Biblioteka(BibliotekaID)
);

CREATE TABLE Uzytkownik (
	UzytkownikID int PRIMARY KEY IDENTITY(1,1),
	Imie varchar(15) NOT NULL,
    Nazwisko varchar(30) NOT NULL,
    Status varchar(10) NOT NULL,
    Login varchar(20) NOT NULL,
    Haslo varchar(20) NOT NULL,
    Typ varchar(20) NOT NULL,
    IndeksPW varchar(6),
    Wypozyczenia int,
    NrTel varchar(9) NOT NULL,
    Email varchar(40) NOT NULL,
);

CREATE TABLE Zamowienie (
	ZamowienieID int PRIMARY KEY IDENTITY(1,1),
	EgzemplarzID int NOT NULL,
    UzytkownikID int NOT NULL,
    Data date NOT NULL,
    CzasOdbioru time NOT NULL,
    FOREIGN KEY (EgzemplarzID) REFERENCES Egzemplarz(EgzemplarzID),
    FOREIGN KEY (UzytkownikID) REFERENCES Uzytkownik(UzytkownikID)
);

CREATE TABLE Wypozyczenie (
	WypozyczenieID int PRIMARY KEY IDENTITY(1,1),
	ZamowienieID int NOT NULL,
    EgzemplarzID int NOT NULL,
    DataWypozyczenia date NOT NULL,
    CzasWypozyczenia time NOT NULL,
    DataZwrotu date NOT NULL,
    FOREIGN KEY (ZamowienieID) REFERENCES Zamowienie(ZamowienieID),
    FOREIGN KEY (EgzemplarzID) REFERENCES Egzemplarz(EgzemplarzID)
);

CREATE TABLE Przedluzenie (
	PrzedluzenieID int PRIMARY KEY IDENTITY(1,1),
	WypozyczenieID int,
    Typ varchar(15),
    Czas time,
    FOREIGN KEY (WypozyczenieID) REFERENCES Wypozyczenie(WypozyczenieID)
);

ALTER TABLE Wypozyczenie ADD PrzedluzenieID int NOT NULL;
ALTER TABLE Wypozyczenie ADD FOREIGN KEY (PrzedluzenieID) REFERENCES Przedluzenie(PrzedluzenieID)

CREATE TABLE Notyfikacja (
	NotyfikacjaID int PRIMARY KEY IDENTITY(1,1),
	PrzedluzenieID int NOT NULL,
    Tresc varchar(200) NOT NULL,
    Typ varchar(15),
    UzytkownikID int NOT NULL,
    FOREIGN KEY (PrzedluzenieID) REFERENCES Przedluzenie(PrzedluzenieID),
    FOREIGN KEY (UzytkownikID) REFERENCES Uzytkownik(UzytkownikID)
);

CREATE TABLE Config (
	ConfigID int PRIMARY KEY IDENTITY(1,1),
	Klucz varchar(30) NOT NULL,
    Wartosc int NOT NULL,
    DataModyfikacji date NOT NULL,
    DataDodania date NOT NULL
);
