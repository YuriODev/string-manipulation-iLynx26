string = input().lower()
clean_string = ""
for char in string:
    if char.isdigit():
        clean_string += char
    elif 97 <= ord(char) <= 122:
        clean_string += char

answer = "Yes" if clean_string == clean_string[::-1] else "No"
print(answer)