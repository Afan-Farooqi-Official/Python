# ==============================================
# Name : Afan Qaiser Farooqi
# Seat No : B23110006006
# Class : BSCS - Section A
# Assignment : Python Practice Assignment
# ==============================================

# --- Q1: Numbers divisible by 7 and multiple of 5 ---
result = []
for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 == 0):
        result.append(i)
print(result)


# --- Q2: Factorial without math.factorial() ----------
num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} = {factorial}")


# --- Q3: Print types from datalist -------------------
datalist = [1452, 11.23, 1+2j, True, 'affan', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print("Value:", item, "| Type:", type(item).__name__)


# --- Q4: Even-digit numbers between 100 and 400  ----
result = []
for i in range(100, 401):
    num = str(i)
    if all(int(digit) % 2 == 0 for digit in num):
        result.append(num)
print(",".join(result))


# --- Q5: Find divisors of a number -------------------
num = int(input("Enter a number: "))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print(f"Divisors of {num} = {divisors}")


# --- Q6: Find common divisors of two numbers ----------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

common_divisors = []
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        common_divisors.append(i)
print(f"Common divisors of {num1} and {num2} = {common_divisors}")


# --- Q7: Find HCF of two numbers ----------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(f"HCF of {num1} and {num2} = {hcf}")


# --- Q8: Calculate area of rectangle -------------------
def rectangle_area(length, width):
    area = length * width
    return area

# Example usage:
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")


# --- Q9: Check if a number is even or odd ---------------

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Example usage:
num = int(input("Enter a number: "))
result = even_or_odd(num)
print(f"The number {num} is: {result}")


# --- Q10: Reverse a string -----------------------------
def reverse_string(s):
    return s[::-1]

# Example usage:
input_string = str(input("Enter a string: "))
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")


# --- Q11: Sum of digits in a number --------------------
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits in {number} is: {result}")


# --- Q12: Check if a number is prime -------------------
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


# --- Q13: Generate Fibonacci sequence -----------------
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Example usage
n = int(input("Enter n: "))
fibonacci(n)


# --- Q14: Count vowels in a string ---------------------
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


# --- Q15: Calculate power of a number -------------------
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