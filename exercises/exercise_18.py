string = input()

multiplication = 1
for char in string:
    if char.isdigit():
        multiplication *= int(char)

print(multiplication)