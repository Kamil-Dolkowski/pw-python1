# Zwrócenie bieżącej daty i godziny:
import datetime
now = datetime.datetime.now()
print(now)

# napisz program, który sprawdza, czy dany format daty jest prawidłowy
# 'dd-mm-yyyy'
todays_date = datetime.date.today()
print(todays_date)

#1 stycznia 1970 - UTC
print(datetime.date.fromtimestamp(1000000000).year)

a = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380).day
print(a)
a = datetime.time(11, 34, 56)
print(a.minute)


now = datetime.datetime.now()
print(now.strftime("%H"))
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(s1)