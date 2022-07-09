# Exercise 34: Validate if two numbers are the same or the sum is five.

def val_num(x,y):
    if x == y or x+y == 5:
        return True

    else:
        return False

print(val_num(3,2))

print(val_num(3,3))

print(val_num(3,4))
    
