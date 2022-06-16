# Write a Python program to convert height (in feet and inches) to centimeters.

h_ft = int(input())
h_inch = int(input())

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)