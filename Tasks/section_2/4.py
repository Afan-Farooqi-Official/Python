# Write a function that takes an integer and returns the sum of all its digits.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits in {number} is: {result}")