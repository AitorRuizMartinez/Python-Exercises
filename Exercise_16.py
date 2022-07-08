# Exercise 16: Create a mathematical funtion.

# f(x) = if x <= 15 => 15 - x; ( 15 - x) * 2

def dif(x):
    if x <= 15:
        return 15 - x
    else:
        return (15-x)*2

print(dif(25))
print(dif(5)) 