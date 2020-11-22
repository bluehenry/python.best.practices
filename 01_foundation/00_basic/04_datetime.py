import calendar
from datetime import datetime, timedelta


def print_dayofweek():
    print(calendar.day_name[0])
    print(calendar.day_name[1])
    print(calendar.day_name[6])


dt = datetime(2019, 8, 17, 00, 00, 00)
h = dt.time().hour
print(h)

d1 = datetime(2020, 2, 11, 8, 52, 40)
d2 = datetime(2020, 2, 11, 9, 52, 40)

print(f'{d1} > {d2}') if d1 > d2 else print(f'{d1} <= {d2}')
