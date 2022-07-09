# Exercise 31: Calculate the LCM of two numbers.

def lcm(x, y):
    z = max(x, y)

    while True:
        if ( z % x == 0) and ( z % y == 0):
            return z

        z += 1

print(lcm(2,4))
print(lcm(33,34))