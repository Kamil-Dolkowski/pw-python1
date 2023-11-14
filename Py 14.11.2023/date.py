# Instrukcje formatowania daty i czasu w Pythonie przy użyciu stfftime() i strptime() są bardzo elastyczne. Oto niektóre z najczęściej używanych dyrektyw formatowania:

# %Y: Rok z pełną liczbą cyfr, np. "2023"
# %m Miesiąc jako liczba z zerem wiodącym, np. "01" do "12"
# %d: Dzien miesiąca jako liczba z zerem wiodącym, np. "01" do "31"
# %H Godzina (zegar 24-godz) jako liczba z zerem wiodącym, np. "00" do "23"
# %I Godzina (zegar 12-godz) jako liczba z zerem wiodącym, np. "01" do "12"
# %M Minuta jako liczba z zerem wiodącym, np. "00" do "59"
# %S Sekunda jako liczba z zerem wiodącym, cp. "00" do "59"
# %f Mikrosekundy jako liczba z zerem wiodącym, np.  "000000" do "999999"

### pip install DateTime

# strftime - format
# strptime - parsowanie (odczytanie w formie zautomatyzowanej)



# Zadanie: Pobierz aktualną datę i czas.
from datetime import datetime
from datetime import date

now = datetime.now()
print(now)
print(now.year)
print(now.strftime("%Y"))

# Wyświetl aktualny miesiąc jako nazwę, np. "Listopad"
print(now.strftime("%b"))

# Aktualny dzień tygodnia
print(now.strftime("%A"))

# Konwertuj napis "2023-11-15" na obiekt daty
date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
print(date_object)

date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
print(date_object)

# Dodaj 5 dni do aktualnej daty.
from datetime import timedelta

date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
new_date = date_object + timedelta(days=5)
print(new_date)

# Odejmij 2 tygodnie od aktualnej daty.
print(now-timedelta(weeks=2))

# Wyświetl różnicę w dniach między 1 stycznia 2023 a dzisiaj
past_date = datetime(2023,1,1)
day = now - past_date
print(day)
print(day.days)

# Sprawdź, czy rok 2024 jest rokiem przestępnym.
import calendar
new_year = calendar.isleap(2024)
print(new_year)

# Wyświetl numer bieżącego tygodnia roku.
print(now.strftime("%U"))

# Zmień format daty z "2023-11-15 00:00:00" na format RFC 2822
rfc_date = datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S +0000")
print(rfc_date)

# Znajdź dzień tygodnia dla 4 lipca bieżącego roku.
date2 = datetime(now.year, 7, 4)
print(date2.strftime("%A"))