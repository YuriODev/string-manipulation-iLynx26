string = input()
has_numbers = False
has_letters = False
for i in range(len(string)):
    if "0" <= string[i] <= "9":
        has_numbers = True
    elif "a" <= string[i] <= "Z":
        has_letters = True

if has_numbers and has_letters:
    print("Your message includes numbers and letters.")
elif has_letters:
    print("Your message includes letters only.")	
elif has_numbers:
    print("Your message includes numbers only.")
