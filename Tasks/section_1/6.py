# Write a program that takes input two integer numbers and prints all the common divisors.
# Example 1: Numbers 100 and 80 → common divisors are 1, 2, 5, 20
# Example 2: Numbers 72 and 90 → common divisors are 1, 2, 3, 6, 18
# Test 1: 100 & 80 → [1, 2, 5, 20] | Test 2: 72 & 90 → [1, 2, 3, 6, 18]

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

common_divisors = []
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        common_divisors.append(i)
print(f"Common divisors of {num1} and {num2} = {common_divisors}")