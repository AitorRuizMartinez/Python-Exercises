# Exercise 49: Show the files in a directory,

from os import listdir
from os.path import isfile, join


rute = r'C:\Users\Aitor\Desktop'

def show_dir(rute):
    files = [a for a in listdir(rute) if isfile(join(rute, a))]

    return files

direc = show_dir(rute)

print(direc)
print(len(direc))