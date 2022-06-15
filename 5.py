# Write a program for handling file operation errors.

filename = 'python.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except Exception as e:
    print(e)