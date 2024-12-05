SELECT *
FROM INFORMATION_SCHEMA.COLUMNS


SELECT *
FROM sys.columns c, sys.tables t WHERE t.object_id = c.object_id


SELECT t.name, c.name AS name_tables
FROM sys.columns c, sys.tables AS t WHERE t.object_id = c.object_id



SELECT t.name, c.name AS 'name tables'                                  <- tak raczej nie
FROM sys.columns c, sys.tables AS t WHERE t.object_id = c.object_id


-- zmiana nazwy kolumny
EXEC sp_rename 'Authors.username', 'username_old', 'COLUMN';
-- zmiana typu kolumny
ALTER TABLE Authors
ALTER COLUMN username_old VARCHAR(100);



SET IDENTITY_INSERT Books ON
SET IDENTITY_INSERT Books OFF



























INSERT INTO Autor (Imie, Nazwisko, Pseudonim)
VALUES ('Jan', 'Kowalski', 'JanKow'),
       ('Anna', 'Nowak', NULL),
       ('Marek', 'Wiśniewski', 'MWisn'),
       ('Karolina', 'Kwiatkowska', 'KKwia'),
       ('Piotr', 'Lis', NULL);

INSERT INTO Gatunek (Nazwa, Ukryj)
VALUES ('Fantastyka', 0),
       ('Kryminał', 0),
       ('Romans', 0),
       ('Biografia', 0),
       ('Science-fiction', 0);

INSERT INTO Wydawnictwo (Nazwa, Status)
VALUES ('Nowa', 'Aktywne'),
       ('Stara', 'Aktywne'),
       ('Orbis', 'Zamknięte'),
       ('Sowa', 'Aktywne'),
       ('Astra', 'Aktywne'),
       ('Vento', 'Zamknięte');
       
INSERT INTO Ksiazka (AutorID, Tytul, GatunekID, Opis, RecenzjaID, RokWydania, WydawnictwoID, Status)
VALUES    (1, 1, 'Fantastyka;, 'Powiesc fantastyczna', 'Mrożący Krew', 4, 2020, 'Sowa', 'Wypożyczona', 101)
    (2, 2, 'Kryminał;, 'Powiesc kryminalna', 'Historyczna Pasja', 5, 2021, 'Nova', 'Wypożyczona', 101)
    (3, 3, 'Romans;, 'Powieść romansowa', 'Romantyczny Raj', 3, 2019, 'Vento', 'Wypożyczona', 101)
    (4, 2, 'Kryminał', 'Powiesc kryminalna', 'Romantyczny Raj', 5, 2019, 'Sowa', 'Wypożyczona', 106),
	(5, 4, 'Science-fiction', 'Powiesc fantastyczna', 'Fantastyczna Przygoda', 4, 2020, 'Orbis', 'Dostępna', 107),
    (6, 5, 'Kryminał', 'Powiesc kryminalna', 'Skrzywdzona Miłość', 5, 2023, 'Nova', 'Wypożyczona', 108),
    (7, 2, 'Romans', 'Powieść romansowa', 'Historyczna Pasja', 3, 2021, 'Orbis', 'Dostępna', 109),
	(8, 3, 'Biografia', 'Literatura faktu', 'Niezwykłe Odkrycie', 4, 2020, 'Nova', 'Dostępna', 110),
    (9, 2, 'Kryminał', 'Powiesc kryminalna', 'Przygnębiający Dramat', 5, 2014, 'Sowa', 'Wypożyczona', 111),
    (10, 4, 'Romans', 'Powieść romansowa', 'Słodki Romans', 3, 2021, 'Astra', 'Dostępna', 112),
	(11, 5, 'Fantastyka', 'Powiesc fantastyczna', 'Zabójcza Zemsta', 4, 2016, 'Vento', 'Dostępna', 113),
    (12, 2, 'Kryminał', 'Powiesc kryminalna', 'Intrygujący Thriller', 5, 2019, 'Orbis', 'Wypożyczona', 114),
    (13, 3, 'Biografia', 'Literatura faktu', 'Science Fiction', 3, 2021, 'Nova', 'Dostępna', 115),
	(14, 2, 'Fantastyka', 'Powiesc fantastyczna', 'Porywająca Fabuła', 4, 2020, 'Vento', 'Dostępna', 116),
    (15, 5, 'Kryminał', 'Powiesc kryminalna', 'Komiczne Przeżycia', 5, 2017, 'Astra', 'Wypożyczona', 117),
    (16, 3, 'Science-fiction', 'Powieść fantastyczna', 'Mrożący Krew', 3, 2021, 'Sowa', 'Dostępna', 118),
	(17, 1, 'Fantastyka', 'Powiesc fantastyczna', 'Złamane Serce', 4, 2023, 'Vento', 'Dostępna', 119),
    (18, 3, 'Kryminał', 'Powiesc kryminalna', 'Mrożący Krew', 5, 2019, 'Nova', 'Wypożyczona', 120),
    (19, 4, 'Biografia', 'Literatura faktu', 'Ucieczka W Czasie', 3, 2021, 'Astra', 'Dostępna', 121),
	(20, 2, 'Fantastyka', 'Powiesc fantastyczna', 'Tragiczne Odkrycie', 4, 2020, 'Orbis', 'Dostępna', 122),
    (21, 3, 'Science-fiction', 'Powiesc kryminalna', 'Zakazana Miłość', 5, 2014, 'Sowa', 'Wypożyczona', 123),
    (22, 3, 'Romans', 'Powieść romansowa', 'Złamane Serce', 3, 2011, 'Nova', 'Dostępna', 124),
	(23, 4, 'Fantastyka', 'Powiesc fantastyczna', 'Ucieczka W Czasie', 4, 2020, 'Sowa', 'Dostępna', 125),
    (24, 2, 'Biografia', 'Literatura faktu', 'Opis drugiej ksiazki', 5, 2019, 'Astra', 'Wypożyczona', 126),
    (25, 3, 'Romans', 'Powieść romansowa', 'Złamane Serce', 3, 2023, 'Vento', 'Dostępna', 127),
	(26, 5, 'Science-fiction', 'Powiesc fantastyczna', 'Mrożący Krew', 4, 2022, 'Sowa', 'Dostępna', 128),
    (27, 2, 'Kryminał', 'Powiesc kryminalna', 'Zakazana Miłość', 5, 2019, 'Nova', 'Wypożyczona', 129),
    (28, 3, 'Romans', 'Powieść romansowa', 'Złamane Serce', 3, 2021, 'Vento', 'Dostępna', 130),
	(29, 5, 'Fantastyka', 'Powiesc fantastyczna', 'Mrożący Krew', 4, 2020, 'Sowa', 'Dostępna', 131),
    (30, 2, 'Biografia', 'Literatura faktu', 'Ucieczka W Czasie', 5, 2019, 'Nova', 'Wypożyczona', 132);
    
INSERT INTO Egzemplarz (BookID, Status, BibliotekaID, Zużycie)
VALUES (1, 'Dostępna', 1, 50),
       (2, 'Wypożyczona', 2, 30),
       (3, 'Dostępna', 1, 70),
       (4, 'Dostępna', 3, 40),
       (5, 'Wypożyczona', 2, 60);

INSERT INTO Lokalizacja (Miasto, Ulica, Numer, KodPocztowy, Wojewodztwo)
VALUES ('Warszawa', 'Aleje Jerozolimskie', 100, '00-001', 'Mazowieckie'),
       ('Kraków', 'Rynek Główny', 1, '30-062', 'Małopolskie'),
       ('Gdańsk', 'Długi Targ', 12, '80-830', 'Pomorskie'),
       ('Wrocław', 'Rynek', 3, '50-106', 'Dolnośląskie'),
       ('Poznań', 'Stary Rynek', 25, '61-772', 'Wielkopolskie');

INSERT INTO Biblioteka (Nazwa, LokalizacjaID, GodzinyOtwarciaID)
VALUES ('Biblioteka Główna', 1, 1),
       ('Biblioteka Uniwersytecka', 2, 2),
       ('Biblioteka Miejska', 3, 3),
       ('Biblioteka Narodowa', 4, 4),
       ('Biblioteka Akademicka', 5, 5);
       
INSERT INTO Zamowienie (EgzemplarzID, UzytkownikID, Data, CzasOdbioru)
VALUES (1, 1, '2023-03-15', '12:00:00'),
       (2, 2, '2023-03-16', '13:30:00'),
       (3, 3, '2023-03-17', '15:45:00'),
       (4, 4, '2023-03-18', '10:15:00'),