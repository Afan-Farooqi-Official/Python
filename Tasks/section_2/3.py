# Write a function that accepts a string and returns its reverse.

def reverse_string(s):
    return s[::-1]

# Example usage:
input_string = str(input("Enter a string: "))
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")