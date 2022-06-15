# Python program to find second largest number in a list

list1 = [10, 20, 99, 4, 45, 99]
new_list = set(list1)
new_list.remove(max(new_list))
print(max(new_list))