# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month of the season (Jan - Dec) in three digit:").lower()
day = int(input("Enter the day of the month in number:"))
if month in ["jan", "feb"]: 
    print(f"{month} {day} is in winter season")
elif month in ["apr", "may"]:
    print(f"{month} {day} is in spring season")
elif month in ["jul", "aug"]:
    print(f"{month} {day} is in summer season")
elif month in ["oct", "nov"]:
    print(f"{month} {day} is in fall season")

# for dec 
if month == "dec" and day > 20: 
    print(f"{month} {day} is in winter season")
elif month == "dec" and day < 21:
    print(f"{month} {day} is in fall season")
# for mar
if month == "mar" and day > 19: 
    print(f"{month} {day} is in spring season")
elif month == "mar" and day < 20:
    print(f"{month} {day} is in winter season")
#for jun
if month == "jun" and day > 20: 
    print(f"{month} {day} is in summer season")
elif month == "jun" and day < 21:
    print(f"{month} {day} is in spring season")    
# for sep
if month == "sep" and day > 21: 
    print(f"{month} {day} is in fall season")
elif month == "sep" and day < 22:
    print(f"{month} {day} is in summer season")
    





