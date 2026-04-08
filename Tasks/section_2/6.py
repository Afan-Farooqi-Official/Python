# Write a function that takes n and prints the first n Fibonacci numbers.
# Example: n=8 → 0 1 1 2 3 5 8 13

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Example usage
n = int(input("Enter n: "))
fibonacci(n)