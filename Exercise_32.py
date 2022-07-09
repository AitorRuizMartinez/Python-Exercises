# Exercise 32: Calculate the sum of three numbers if they're are not similar, if similar the sum will be zero.

def sum(x, y,z):
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z

print(sum(2,3,4))
print(sum(2,2,2))