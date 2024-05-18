string = input() + "*"
coded_string = ""

same_char_count = 0
previous_char = string[0]

chars_left = len(string)

for char in string:
    if char == previous_char and chars_left > 1:
        same_char_count += 1
    else:
        coded_string += previous_char
        coded_string += str(same_char_count)
        same_char_count = 1
    previous_char = char
    chars_left -= 1

print(coded_string)