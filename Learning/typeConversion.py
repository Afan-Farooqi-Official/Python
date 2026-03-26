# integer conversion
birth_year = input("Enter your birth year: ")
# The input function returns a string, so we need to convert it to an integer before performing arithmetic operations.

current_year = 2026
age = current_year - int(birth_year)
print("Your age is: " + str(age))

# float conversion
weight = input("Enter your weight in kg: ")
# The input function returns a string, so we need to convert it to a float before performing arithmetic operations.
weight_in_pounds = float(weight) * 2.20462
print("Your weight in pounds is: " + str(weight_in_pounds))
