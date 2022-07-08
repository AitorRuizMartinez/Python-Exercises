# Exercise 17: Create a function to evaluate if a number is close to 1000 or 2000.

def close(x):
    if  900 <= x <= 1100:  
        return " It is close to 1000"
    elif 1900 <= x <= 2100: 
        return "It is close to 2000"
    else:
        return  " It is not close to 1000 or 2000"

print(close(900))