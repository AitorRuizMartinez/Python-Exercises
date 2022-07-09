# Exercise 23: Check if a character is a vowel.

# c = 'i', ['a','e','i','o','u'] => True
# c = 'v', ['a','e','i','o','u'] => False

def is_vowel(c):

    if len(c) == 1:
        vowels = 'aeiou'
        c = c.lower()
        
        return c in vowels

    else:
        return False



print(is_vowel('a'))
print(is_vowel('b'))
print(is_vowel('o'))
print(is_vowel('oei'))