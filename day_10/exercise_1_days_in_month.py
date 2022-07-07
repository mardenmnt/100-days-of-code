
"""
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)

And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
"""

def is_leap(year):
    """This function checks if the informed year is a leap year or not"""   # DocString
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """This function returns the number of days in the given month"""   # DocString
    if month > 12 or month < 1:
        return "Invalid month"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
     

    ### OR ###

    # if month in [1,3,5,7,8,10,12]:
    #     return 31
    # elif month in [4,6,9, 11]:
    #     return 30
    # elif is_leap(year) == False:
    #     return 28
    # else:
    #     return 29

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)