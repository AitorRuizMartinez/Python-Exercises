# Exercise 7: Get the extension name of a file.

# main.py

filename = input('What is the name of your file: ')

filenametype = filename.split('.')

print(filenametype)

print(filenametype[-1])
