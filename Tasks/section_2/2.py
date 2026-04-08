# Write a function that takes an integer and returns whether it is Even or Odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Example usage:
num = int(input("Enter a number: "))
result = even_or_odd(num)
print(f"The number {num} is: {result}")