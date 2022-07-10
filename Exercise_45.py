# Exercise 45: Execute a command using call function.

from subprocess import call

print(call(['ping', 'google.com']))