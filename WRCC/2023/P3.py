# WRCC Friday 13

import datetime

monthToNumber = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

daysTillFri = {
    "Friday": 0,
    "Thursday": 1,
    "Wednesday": 2,
    "Tuesday": 3,
    "Monday": 4,
    "Sunday": 5,
    "Saturday": 6
}

count = 0

weekDayStart, month, day, year = input().replace(",", "").split()

dateStart = datetime.datetime(int(year), monthToNumber[month], int(day))

weekDayEnd, month, day, year = input().replace(",", "").split()

dateEnd = datetime.datetime(int(year), monthToNumber[month], int(day))

dateStart = dateStart.__add__(datetime.timedelta(days=daysTillFri[weekDayStart]))

# print(dateStart.day)

while dateStart < dateEnd:
    if dateStart.day == 13:
        count += 1
    dateStart = dateStart.__add__(datetime.timedelta(days=7))

print(count)
