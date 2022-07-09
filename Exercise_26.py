# Exercise 26: Emulate the join function.

numbers = [2, 5, 6, 3, 19]

print(''.join([str(n) for n in numbers]))

def join_list(list):
    result = ''

    for i in list:
        result += str(i)

    return result

print(join_list(numbers))