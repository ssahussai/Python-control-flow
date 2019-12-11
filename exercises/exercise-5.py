# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it


terms = int(input("Enter term:"))
n1 = 0
n2 = 1
count = 0

if terms <= 0:
    print("Enter a positive number!")
elif terms == 1:
    print(f"Fibonacci sequence: {n1}")
elif terms < 51:
    print("Fibonacci sequences:")
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2 = nth
        count += 1
else: 
    print("This function goes only upto 50 terms!")

