import holidays
from datetime import date

#Curent Year
year = 2025

# Get US holidays for the given year
us_holidays = holidays.UnitedStates(years=year)

# Print all holidays
print(f"US Holidays in {year}:\n")
for day, name in sorted(us_holidays.items()):
    print(f"{day}: {name}")