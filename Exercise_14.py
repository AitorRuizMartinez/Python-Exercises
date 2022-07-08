# Exercise 14: Calculate the difference between two given dates.

from datetime import date

today = date(2022,1,23)
another_day = date(2034,2,12)

diff = another_day - today

print(diff.days)