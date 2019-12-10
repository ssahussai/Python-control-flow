# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


side_a = input("Enter the lengths of 1 side of a triangle:")
side_b = input("Enter the lengths of 2 side of a triangle:")
side_c = input("Enter the lengths of 3 side of a triangle:")
if (side_a == side_b == side_c):
    print(f"A triangle with sides of {side_a}, {side_b}, & {side_c} is a equalateral")
elif side_a == side_b or side_a == side_c:
    print(f"A triangle with sides of {side_a}, {side_b}, & {side_c} is a isosceles")
elif (side_a != side_b != side_c):
    print(f"A triangle with sides of {side_a}, {side_b}, & {side_c} is a scalene")


    
