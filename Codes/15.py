# Python program to print all Prime numbers in an Interval

start = 2
end = 20
lst = []

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           lst.append(num)

if len(lst)==0:
    print("No prime numbers were found")
else:
    print(lst)


