number = int(input())
string = input()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

new_string = ""

for char in string:
    if char.lower() == char:
        index = (alphabet.index(char)+number) % 26
        new_string += alphabet[index]
    else:
        char = char.lower()
        index = (alphabet.index(char)+number) % 26
        new_string += alphabet[index].upper()

print(new_string)