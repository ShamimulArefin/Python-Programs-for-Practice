# Python program to print even length words in a string

s = "This is a python language"
s = s.split(" ")

for i in s:
    if len(i)%2==0:
        print(i)