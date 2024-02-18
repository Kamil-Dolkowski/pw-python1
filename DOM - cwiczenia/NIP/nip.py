import requests

def dane_z_nip(nip: int, date:str):
    try:
        url = f"https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={date}"
        response = requests.get(url)
        name = response.json()["result"]["subject"]["name"]
        address = response.json()["result"]["subject"]["workingAddress"]
        status = response.json()["result"]["subject"]["statusVat"]
        regon = response.json()["result"]["subject"]["regon"]
        registractionLegalDate = response.json()["result"]["subject"]["registrationLegalDate"]
        accountNumbers = response.json()["result"]["subject"]["accountNumbers"]

        print("\n------------DANE------------")
        print(f"Nazwa: {name}")
        print(f"NIP: {nip}")
        print(f"Adres: {address}")
        print(f"Status: {status}")
        print(f"Regon: {regon}")
        print(f"Data zarejestrowania: {registractionLegalDate}")
        print(f"Numery kont: ")
        i=1
        for account in accountNumbers:
            print(f"{i}. {account}")
            i+=1

    except TypeError:
        print("\nBrak informacji.")
    except KeyError:
        print("\nBrak informacji.")
        message = response.json()["message"]
        print(message)

def validate_nip(nip):
    if len(nip) != 10:
        return False
    if not str(nip).isdigit():
        return False
    wagi = [6,5,7,2,3,4,5,6,7]
    suma = 0
    for i in range(0,9):
        suma += int(nip[i])*wagi[i]
    if suma%11 == int(nip[9]):
        return True
    else:
        return False


from datetime import datetime

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False




# dane_z_nip(5260250274,"2019-12-13")


nip = input("\nWprowadź NIP: ")
if not validate_nip(nip):
    print("Nieprawidłowy NIP.")
else:
    date = input("Wprowadź datę (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Nieprawidłowy format daty.")
    else:
        dane_z_nip(nip, date)











#------------------------------PRZYKŁAD-----------------------------------


# https://wl-api.mf.gov.pl/api/search/nip/5260250274?date=2019-12-13


# {"result":{"subject":{"name":"MINISTERSTWO FINANSÓW","nip":"5260250274","statusVat":"Czynny","regon":"000002217","pesel":null,"krs":null,"residenceAddress":null,"workingAddress":"ŚWIĘTOKRZYSKA 12, 00-916 WARSZAWA","representatives":[],"authorizedClerks":[],"partners":[],"registrationLegalDate":"1996-01-01","registrationDenialBasis":null,"registrationDenialDate":null,"restorationBasis":null,"restorationDate":null,"removalBasis":null,"removalDate":null,"accountNumbers":["12101010100075912221000000","59101010100075912222000000","41101010100071712231000000","64101010100037242231000000","18101010100046042231000000","06101010100075912225000000","03101010100075912227000000","10101010100038252231000000","18101014690032611391200000","64101010100075911339200000","78113010170200000000137228","07113010170200000000138215","59113010880001312263200002","49101010100038122225000000","09101010100075912223000000","60101010100038252230000000"],"hasVirtualAccounts":false},"requestId":"LaNA1-8mck7ch","requestDateTime":"18-02-2024 14:41:05"}}

# {"result":
#  {"subject":
#   {"name":"MINISTERSTWO FINANSÓW",
#    "nip":"5260250274",
#    "statusVat":"Czynny",
#    "regon":"000002217",
#    "pesel":null,
#    "krs":null,
#    "residenceAddress":null,
#    "workingAddress":"ŚWIĘTOKRZYSKA 12, 00-916 WARSZAWA",
#    "representatives":[],
#    "authorizedClerks":[],
#    "partners":[],
#    "registrationLegalDate":"1996-01-01",
#    "registrationDenialBasis":null,
#    "registrationDenialDate":null,
#    "restorationBasis":null,
#    "restorationDate":null,
#    "removalBasis":null,
#    "removalDate":null,
#    "accountNumbers":["12101010100075912221000000","59101010100075912222000000","41101010100071712231000000","64101010100037242231000000","18101010100046042231000000","06101010100075912225000000","03101010100075912227000000","10101010100038252231000000","18101014690032611391200000","64101010100075911339200000","78113010170200000000137228","07113010170200000000138215","59113010880001312263200002","49101010100038122225000000","09101010100075912223000000","60101010100038252230000000"],
#    "hasVirtualAccounts":false},
#    "requestId":"LaNA1-8mck7ch",
#    "requestDateTime":"18-02-2024 14:41:05"}}