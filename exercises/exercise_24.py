string = input()

overall_characters = len(string)
lowercase_characters = 0
uppercase_characters = 0

for char in string:
    if char.upper() != char:
        lowercase_characters += 1
    elif char.lower() != char:
        uppercase_characters += 1
    else:
        overall_characters -= 1


if overall_characters != 0:
    lowercase_percentage = lowercase_characters / overall_characters * 100
    uppercase_percentage = uppercase_characters / overall_characters * 100

    print(f"{lowercase_percentage:.2f}")
    print(f"{uppercase_percentage:.2f}")
else:
    print("0.00")
    print("0.00")