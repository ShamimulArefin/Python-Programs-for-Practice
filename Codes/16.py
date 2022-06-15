# Python Program for How to check if a given number is Fibonacci number

def is_fib_number(num):
    a = 0
    b = 1
    while b<num:
        c = a+b
        a = b
        b = c
    if b==num or a==num:
        return True
    if b > num:
        return False

num = 34
if is_fib_number(num):
    print(f"{num} is a fibonacci number.")
else:
    print(f"{num} is not a fibonacci number.")