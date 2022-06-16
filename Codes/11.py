# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(a, b):
    if a==0 or b==0:
        return ((a, b)[a==0])
    return gcd(b%a, a)


print(gcd(10, 15))