# Program to count the number of each vowel in a string.

s = input()
s = s.lower()
vowels = {}
for vowel in "aeiou":
    cnt = s.count(vowel)
    vowels[vowel] = cnt
print(vowels)