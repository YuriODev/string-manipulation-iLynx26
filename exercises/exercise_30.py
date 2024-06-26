string = input() + "*"

dict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
    "*": 0
}

next_char = ""

number = 0
i = 0

while i < len(string) - 1:
    char = string[i]
    next_char = string[i+1]

    current_number = dict[char]
    next_number = dict[next_char]

    if next_number > current_number:
        number += next_number - current_number
        i += 2
    else:
        number += current_number
        i += 1

print(number)

# Prompt the user to enter a Roman numeral
# roman_numeral = input("Enter a Roman numeral: ")

# # Initialize the integer value of the Roman numeral
# integer_value = 0

# # Initialize the previous value of the Roman numeral
# previous_value = 0

# # Iterate through the Roman numeral in reverse
# for i in range(len(roman_numeral)-1, -1, -1):
#     # Get the value of the Roman numeral
#     char = roman_numeral[i]
#     # Check if the character is 'I'
#     if char == 'I':
#         value = 1
#     # Check if the character is 'V'
#     elif char == 'V':
#         value = 5
#     # Check if the character is 'X'
#     elif char == 'X':
#         value = 10
#     # Check if the character is 'L'
#     elif char == 'L':
#         value = 50
#     # Check if the character is 'C'
#     elif char == 'C':
#         value = 100
#     # Check if the character is 'D'
#     elif char == 'D':
#         value = 500
#     # Check if the character is 'M'
#     elif char == 'M':
#         value = 1000
#     # Subtract the value from the integer value if it is less than the previous value
#     if value < previous_value:
#         integer_value -= value
#     # Add the value to the integer value if it is greater than or equal to the previous value
#     else:
#         integer_value += value
#     # Update the previous value
#     previous_value = value

# # Print the integer value of the Roman numeral
# print(integer_value)
