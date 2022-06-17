# Write a Python program to print the calendar of a given month and year.

import calendar

y = int(input())
m = int(input())

print(calendar.month(y, m))