# Write a Python program to create a histogram from a given list of integers.

n = [2, 3, 5, 4, 7]

for i in n:
    histogram = ""
    while i>0:
        histogram = histogram + 'x'
        i -= 1
    print(histogram)
        
