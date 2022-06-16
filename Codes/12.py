# Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(a, b):
    x = (a, b)[a>b]
    while True:
        if x%a==0 and x%b==0:
            result = x
            break
        x+=1
    return result


print(lcm(54, 24))