# Write a function that accepts a string and returns the count of vowels in it.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage:
input_string = str(input("Enter a string: "))
vowel_count = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {vowel_count}")