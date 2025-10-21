# Dyski (Storage):
- HDD
- SSD
- M.2
- Pendrive
- taśma magnetyczna
- karta micro SSD
- płyta CD
- płyta DVD
- dyskietka

## Jak zabezpieczyć?:
- kolejność: SSD, HDD, płyta
- metoda 3,2,1

# Storage w chmurze:
- są wysoko skalowalne, elastyczne
- dostęp przez http
- dostęp z całego świata
- trwałość i redundancja

## Redundancja:
- LRS - 3 kopie danych w 1 strefie (non-critical)
- ZRS - 3 kopie danych w 2 miejscach (6 kopii) (cirtical)
- 

region - np. Frankfurt, we Frankfurcie są np. 3 strefy

&nbsp;

# Konto magazynu (Storage Account)

## Typy:
- Azure Blob Storage (dane niestrukturyzowane, np. zdjęcia, filmy, word, pliki binarne, statyczne strony)
- Azure Files (pliki do maszyn wirtualnych, uwierzytelnianie, synchronizacja plików z serwerami lokalnymi)
- Azure Queue Storage (duża ilość komunikatów, 64kB - 1 komunikat, interfejs oparty na REST)
- Azure Table Storage (dla nieustrukturyzowanych danych, klucz-wartość, brak narzuconego schematu, skalowanie, niski koszt przechowywania, logi, dane z IoT)
---
- block blobs - duże ilości danych, multimedia
- file shares
- page blobs (stronnicowe) - 512 B, losowy odczyt i zapis
- append blobs - dual channel, logowanie i audyt

## Access tier (warstwy dostępu):
- optymalizacja kosztów
- jak często korzystanie z danych
- hot - najwyższa wydajność i koszt, do aktywnych danych
- cool - niższy koszt, wyższy koszt dostępu (dane na 30 dni)
- cold - najniższa wydajność i koszt (dane nie częściej niż pół roku)

Azure Elastic SAN

## Encription type: 
- Microsoft-managed keys (MMK)
- Customer-managed keys (CMK)

&nbsp;

# Konwencje nazewnictwa:
- Azure Naming Tool
- sprawdzane w prehookach, code review
- bezpieczeństwo - nazwa środowiska (prod, dev)
- grupowanie, tagowanie
- coplience and auditing
- skalowalność
- łatwość zidentyfikowania zasobu
---
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming
- używanie małych liter
- unikanie znaków specjalnych, tylko (a-z)(0-9)(-)
- maksymalna czytelność
---
- rg - resource group
- vm - virtual machine
- st - storage
- app - application
- vnet - virtual network
---
- dev - środowisko deweloperskie
- test - środowisko testowe
- staging - środowisko preprodukcyjne
- prod - środowisko produkcyjne
- sandbox - środowisko sandboxowe, do ustabilizowania infrastruktury przy poważnych zmianach
- demo - środowisko z danymi nieprodukcyjnymi