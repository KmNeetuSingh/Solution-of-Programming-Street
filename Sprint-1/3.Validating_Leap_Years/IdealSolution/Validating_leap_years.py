def is_leap_year(year):
    if year % 400 == 0:
        return "Leap year"
    elif year % 100 == 0:
        return "Not a Leap Year"              """Here we divided by 100 to keeps the calendar year aligned with the Earth's Orbit"""
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Usage...
year = 2020
print(is_leap_year(year))
