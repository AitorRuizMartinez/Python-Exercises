# Exercise 33: Sum of two numbers. If the sum is between 10 and 30, return 30.

def sum(x,y):
    sum_op = x + y
    
    if sum_op >= 10 and sum_op <= 30:
        return 30

    else:
        return sum_op

print(sum(10,25))