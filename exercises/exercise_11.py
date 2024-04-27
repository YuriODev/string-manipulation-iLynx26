string = input()
reversed_string = string[::-1]

if " " in string:
    indx = reversed_string.index(" ")
    word = string[indx:]
else:
    word = string

print(word)