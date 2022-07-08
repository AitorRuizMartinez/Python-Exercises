# Exercise 3: Get system current date.

import datetime

now = datetime.datetime.now()

print(now)

print(type(now))

print(now.strftime('%d/%m/%Y %H:%M:%S'))