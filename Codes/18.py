# Write a program to remove duplicate elements from list.

lst = ['a', 'b', 'a', 'c', 'c', 'd', 'e']
lst = list(set(lst))
print(lst)

# another
l = ["a", "b", "e", "c", "d", "e", "a", "c"]
l = list(dict.fromkeys(l))
print(l)