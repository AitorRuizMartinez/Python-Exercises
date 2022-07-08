# Exercise 6: Get a group of numbers separated by coma and make a list.

# 2, 5, 3, 4 ,1

numbers = input('Write your numbers separated by coma: ')

print(numbers)
print(type(numbers))  

numberslist = numbers.split(',')
print('--------------------------------')
 
print(numberslist)
print(type(numberslist))  
