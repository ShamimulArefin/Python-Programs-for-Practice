# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

d_ft = int(input())

print("The distance in inches is %i inches." % (d_ft * 12))
print("The distance in yards is %.2f yards." % (d_ft / 3.0))
print("The distance in miles is %.2f miles." % (d_ft / 5280.0))
