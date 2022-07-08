# Exercise 9: Show a date saved in a tuple.

from calendar import month


event_date=(2014,10,11)

print(type(event_date))

print('The event is on: %i/%i/%i' % event_date)

print('------------------------')
year, month, day = event_date

print('The event is on: {}/{}/{}'.format(year,month,day))