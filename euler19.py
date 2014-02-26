numSun = 0
day = 1
daysOfMonth = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
for year in range(1900,2001):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        daysOfMonth[1] = 29
    else:
        daysOfMonth[1] = 28
    for month in range(0,12):
        day = day %7
        print(year, day, month)
        if day == 0 and year > 1900:
            numSun += 1
        day += daysOfMonth[month]%7
print (numSun)
