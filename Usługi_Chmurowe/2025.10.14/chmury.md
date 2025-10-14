## Narzędzia:
- DevOps
- Entra - zarządzanie zasobami (Active Directory)
- GitHub
- Microsoft 365 Admin
- Visual Studio code

## Narzędzia:
- Function App
- Azure Cosmo DB
- App Services
- Storage accounts
- Virtual Networks
- Microsoft Entra ID
- Monitor
- Advisor - analiza rekomendacji, optymalizacja
- Microsoft Defender for Cloud
- Cost Management + Billing

portal.azure.com

google cloud console

Microsoft 365 -> SaS

## Cechy chmury:
- dostęp do zasobów na żądanie
- szybki dostęp do sieci
- transfer do chmury jest za darmo, ale wyciągnięcie danych z chmury jest płatne
- najnowsze gateway'e, walidacje
- globalny storage
- pula zasobów, skalowalność
- elastyczne zarządzanie i tworzenie maszyn
- mierzenie i zarządzanie zasobami

---

Azure Cloud Shell

## Subskrypcje

subskrypcja - podpięcie pod konto, które finansuje

subskrypcje - wydzielenie poszczególnych projektów

- budżet
- tagi - kategoryzacja zasobów i grup

---

- Overview
- Activity log
- Access control (IAM)
- Events
- Resource Groups
- Cost Management
- Billing

***Best Practise:***
- zmniejszenie uprawnien dla Ownera, w celu bezpieczeństwa
- użytkownik, do którego nie da się zalogować z zewnątrz

## Resource Groups - grupy zasobów

grupy zasobów - pokoje, w których są dane zasoby

- elastyczne zarządzanie zasobami
- wydzielenie mikroserwisu, współdzielonego zasobu

resource JSON - skrypt, który opisuje jak powstał i gdzie jest przypisana grupa zasobów

azure templates - wersjonowanie w gitcie

# Stworzenie wirtualnej maszyny

All Services -> All -> Virtual Machines

hybryda - chcemy użyc mocy obliczeniowej, a dane mamy u siebie

Create virtual machine -> 

```
Resource group: VM
Virtual machine name: Ubuntu
Region: (Europe) US South
Authentication Type: Password
Ports: HTTP, HTTPS
```

```
Disk: Image default (30GiB)
Standard SSD (locally-redundant storage)
Platform-managed key
```

Wejście przez SSH do VM'ki

Virtual Network -> Create virtual network -> Create a new IP address pool

---

Bastion - "przesiadka" między wirtualkami, przez niego wchodzi się do wirtualek ?

Microsoft Learn - szkolenia

terraform

az - polecenie w terminalu do zarządzania chmurą