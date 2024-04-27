string = input()

number = ""
for char in string:
    if "0" <= char <= "9":
        number += char

print(number)