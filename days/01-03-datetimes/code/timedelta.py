from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours = 10)

print(type(t))
print(t.days)
print(t.seconds)

print(t.seconds / 60 / 60)  # Convert seconds to hours

eta = timedelta(hours=6)

today = datetime.today()

print(today)
print(eta)


print(today + eta) # Add timedelta to current datetime

print(str(today + eta))  # Convert to string for display