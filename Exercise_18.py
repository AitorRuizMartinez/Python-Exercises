# Exercise 18: Calculate the sum of three numbers and include an equal comparison.

def sum_num(a,b,c):
    
    sum = a + b + c

    if a == b and a == c:
        sum *= 3 
    
    return sum

print(sum_num(2,2,2))