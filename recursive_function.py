# Factorial Calculation
def factotial(n):
    if n == 0:
        return 1
    else:
        return n * factotial(n-1)
    
fact = factotial(6)
print(fact)

#Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fib = fibonacci(10)
print(fib)

#Sum of a List
def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0]  + recursive_sum(lst[1:])
    
numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))

#String Reversal
def reverse_string(s):
    if len(s) == 0:
        return s 
    else:
        return reverse_string(s[1:]) + s[0]
    
text = "hello"
print(reverse_string(text))

#------------------------------------------------------------------------------------------------------#

import calendar

# Custom holidays 
custom_holidays = ["2024-09-18", "2024-09-24"]

# Function to check if a day is a holiday
def is_holiday(year, month, day):
    day_str = f"{year}-{month:02d}-{day:02d}"
    weekday = calendar.weekday(year, month, day)

    # Check if it's Saturday (5) or Sunday (6)
    if weekday in [5, 6]:
        return True
    # Check if it's a custom holiday
    if day_str in custom_holidays:
        return True
    return False

# Recursive function to list holidays in the month
def list_holidays(year, month, day=1, holidays=None):
    if holidays is None:
        holidays = []

    # Get the total number of days in the month
    _, total_days = calendar.monthrange(year, month)

    # Base case: If day exceeds the total days in the month, return the list
    if day > total_days:
        return holidays

    # Check if the current day is a holiday
    if is_holiday(year, month, day):
        holidays.append(f"{year}-{month:02d}-{day:02d}")

    # Recursive call to check the next day
    return list_holidays(year, month, day + 1, holidays)

# Example usage
year = 2024
month = 9  # September
holidays = list_holidays(year, month)

# Print the list of holidays
print("Holidays in the month:")
for holiday in holidays:
    print(holiday)


