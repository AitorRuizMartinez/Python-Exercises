# Exercise 48: Transform a string to int and real.

string = '3.1415'

int_num = int(string.split('.')[0])

real = float(string)

print(string)
print(int_num)
print(real)