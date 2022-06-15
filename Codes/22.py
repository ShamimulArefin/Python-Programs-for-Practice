# Python Program to check if a string contains any special character

s = "code#alap!"
special = "[@_!#$%^&*()<>?/\|}{~:]"
flag = False
for i in s:
    if i in special:
        flag = True
        break
if flag:
    print("It contains special character")
else:
    print("It does not contain special character")