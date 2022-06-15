# Python Count the Number of matching characters in a pair of string

str1 = 'aabcddekll12@'
str2 = 'bb2211@55k'
str1, str2 = set(str1), set(str2)

print(len(str1.intersection(str2)))
# or
print(len(str1 & str2))