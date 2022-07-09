# Exercise 25: Create a histogram from a int list.

# [4 ,5 ,1, 8]


# ****
# *****
# *
# ********

def histogram(list, character='*'):
    for i in list:
        print(character * i)

histogram([8,15,6,19])
