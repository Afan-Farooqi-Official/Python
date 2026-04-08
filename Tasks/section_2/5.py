# Write a function that takes a number and returns True if it is prime, otherwise False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
number = int(input("Enter a number: "))
result = is_prime(number)
print(f"The number {number} is prime: {result}")