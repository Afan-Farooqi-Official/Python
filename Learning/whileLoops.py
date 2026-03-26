# while loop

i = 1
while i <= 5:
    print(i)
    i += 1

print('******************************')

# while loop with else
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("i is greater than 5")

print('******************************')

# while loop with break
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("i is greater than 5")

print('******************************')

# while loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

print('******************************')

# pyramid pattern using while loop
n = 5
i = 1
while i <= n:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    i += 1
