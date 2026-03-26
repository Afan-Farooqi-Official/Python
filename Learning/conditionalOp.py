# conditional operation

a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

print('*************************************')

# nested if
age = 90
if age >= 18:
    if age < 65:
        print("adult")
    else:
        print("senior")
else:
    print("not an adult")

print('*************************************')

# ternary operator
age = 25
status = "adult" if age >= 18 else "not an adult"
print(status)

print('*************************************')

# switch case (using dictionary)

operation = input("Enter operation (add, subtract, multiply, divide): ")

match operation:
    case "+":
        print("You chose addition")
    case "-":
        print("You chose subtraction")
    case "*":
        print("You chose multiplication")
    case "/":
        print("You chose division")
    case _:
        print("Invalid operation")