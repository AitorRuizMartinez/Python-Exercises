# Exercise 22: Create a substring of n characters multiplicated n times.

# 'Python', n = 2 => 'Py'; 'PyPy'

from operator import mul


def mulsubstring(string, n):
    n_characters = n

    if n_characters > len(string):
        n_characters = len(string)

    substring = string[0:n_characters]

    result = ''

    for i in range(n):
        result += substring

    return result


print(mulsubstring('Python', 2))