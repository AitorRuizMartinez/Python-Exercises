# Exercise 19: Evaluate if a string ends with .py extension, if not you have to add it.

# main -> main.py

def file_name(file):
    if len(file) >= 3 and file[-3:] == '.py':
        return file
    return file + '.py'

print(file_name('main.py'))
print(file_name('module'))