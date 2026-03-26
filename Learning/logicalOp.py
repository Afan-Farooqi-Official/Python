# logical operators

a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# example
price = 5
if price > 0 and price > 10:
    print("price is a positive single-digit number")

size = 15
if size < 0 or size > 10:
    print("size is not a single-digit number")
