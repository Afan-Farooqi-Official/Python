# Write a program that prints Factorial of a user given integer without using math.factorial() function.
# Example: Enter 5 → Factorial of 5 = 120

num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} = {factorial}")