string = input()

word_count = 1

for char in string:
    if char == " ":
        word_count += 1

print(word_count)