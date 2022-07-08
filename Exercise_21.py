# Exercise 20: Generate the n first even numbers.

def even_numbers(n):
    even = []

    count = 0
    number = 0

    while count < n:
        if number % 2 == 0:
            even.append(number)
            count += 1

        number += 1
    return even

print(even_numbers(50))

