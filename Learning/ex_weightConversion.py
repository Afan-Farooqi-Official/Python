
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ").upper()

if unit == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("Invalid unit")