# Program to display calendar of the given month and year
# author; MoneiBK
# importing calendar module
import calendar
import datetime

yy = 2021  # year
mm = 7   # month
dd = 21 # day of the chosen month

# Current Date and Time
x = datetime.datetime.now()
print(x)


# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
# dd = int(input("Enter day: ")

# display the calendar
print(calendar.month(yy, mm))
