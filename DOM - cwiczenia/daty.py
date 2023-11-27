import datetime
now = datetime.datetime.now()
print(now)

# now1 = datetime.date.today()
# print(now1)

# print(datetime.date.fromtimestamp(10000000).year)

# a = datetime.datetime(2023,1,23,22,34,2).day
# print(a)
# a=datetime.time(12,15,20)
# print(a.second)

# print(now.strftime("%B"))


# print(now)
# d1 = now.strftime("%H:%M:%S %a, %d %b %Y")
# print(d1)






from datetime import datetime
date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
print(date_object)

date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
print(date_object)

print(now)
from datetime import timedelta
date = now + timedelta(days=7)
print(date)
date1 = datetime.strptime("2023-11-20", "%Y-%m-%d")
roznica=(now-date1).
print(roznica)