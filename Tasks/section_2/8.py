# Write a function that computes base^exponent without using the ** operator or pow().

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage:
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")