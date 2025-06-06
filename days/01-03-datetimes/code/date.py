from datetime import datetime
from datetime import date

print(type(datetime.today()))
print(datetime.today())\

todaydate = date.today()
print(type(todaydate))
print(todaydate)
print(todaydate.year)
print(todaydate.month)
print(todaydate.day)

christmas = date(2025, 12, 25)

if christmas != todaydate:
    print("Sorry, there are still", (christmas - todaydate).days, "days until Christmas!")