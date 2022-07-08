# Exercise 10: Ask the user a number 'n' and calculate n + nn + nnn

# n = 3 => 3 + 33 + 333 = 369

n = input('Write the value of n: ')

nn = int('{}{}'.format(n,n))
nnn = int('{}{}{}'.format(n,n,n))
n = int(n)

calculate = n + nn + nnn

print(calculate)