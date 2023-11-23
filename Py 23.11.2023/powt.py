# Zadanie: Pobierz aktualną datę i czas.

from datetime import datetime
now=datetime.now()
print(now)

# Zadanie: Wyświetl aktualny rok.

print(now.year)

# Zadanie: Wyświetl aktualny miesiąc jako nazwę, np. "Listopad".

import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')
print(now.strftime("%B"))



# Zadanie: Dodaj 5 dni do aktualnej daty.

from datetime import timedelta
print(now+timedelta(days=5))

# Zadanie: Odejmij 2 tygodnie od aktualnej daty.

print(now-timedelta(weeks=2))

# Zadanie: Oblicz wiek osoby urodzonej w dniu "1990-05-28".

date1=datetime.strptime("1990-05-28","%Y-%m-%d")
roznica = now.year-date1.year
print(roznica)






# Zadanie: Napisz program, który czyta plik tekstowy i wyświetla jego zawartość.
