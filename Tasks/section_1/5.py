# Write a program that takes input an integer number and prints all of its Divisors.
# Example: Enter 100 → Divisors: [1, 2, 4, 5, 10, 20, 25, 50, 100]

num = int(input("Enter a number: "))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print(f"Divisors of {num} = {divisors}")