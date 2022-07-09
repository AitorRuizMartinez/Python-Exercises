# Exercise 24: Simulate the function of the operator in.

print(5 in [2,4,5,6,3,12])
print('e' in 'Tennis')
print('e' in 'World')

def inside(list, element):
    for e in list:
        if element == e:
            return True

    return False

print(inside('Coding','i'))