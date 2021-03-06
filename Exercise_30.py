# Exercise 30: Calculate GCD of two numbers.

def gcd(x ,y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break

    return gcd

print(gcd(8,4))

print(gcd(13,7))