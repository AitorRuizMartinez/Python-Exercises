# Exercise 20: Simulate a string multiplication.

def mult_string(string, multiplication):
    result = ""

    for i in range(multiplication):
        result += string

    return result

print(mult_string('Hi ', 3))