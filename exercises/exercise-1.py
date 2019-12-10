# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

alphabet = input('Please enter a letter from the alphabet (a-z or A-Z):').lower()
if alphabet == "a":
    print("The letter a is a vowel")
elif alphabet == "e":
    print("The letter e is a vowel")
elif alphabet == "i":
    print("The letter i is a vowel")
elif alphabet == "o":
    print("The letter o is a vowel")
elif alphabet == "u":
    print("The letter u is a vowel")
else:
    print("You've entered a consonant!")


