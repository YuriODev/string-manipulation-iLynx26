char_1 = input()
char_2 = input()

output = ""

for i in range(255):
    if char_1 <= str(chr(i)) <= char_2:
        output += str(chr(i))
    elif chr(i) > char_2:
        break
    
print(output)
