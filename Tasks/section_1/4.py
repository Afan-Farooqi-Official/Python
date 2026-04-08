# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a
# number is an even number. The numbers obtained should be printed in a comma-separated sequence.
# Output: 200,202,204,206,208,220,222, ... ,488

result = []
for i in range(100, 401):
    num = str(i)
    if all(int(digit) % 2 == 0 for digit in num):
        result.append(num)
print(",".join(result))