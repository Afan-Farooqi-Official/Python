# Extend the logic of last object: write a program that takes input two integer numbers and prints the
# Highest Common Factor (also called Greatest Common Divisor).
# Example 1: Numbers 100 and 80 → HCF = 20
# Example 2: Numbers 72 and 90 → HCF = 18
# Test 1: 100 & 80 → HCF = 20 | Test 2: 72 & 90 → HCF = 18

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(f"HCF of {num1} and {num2} = {hcf}")