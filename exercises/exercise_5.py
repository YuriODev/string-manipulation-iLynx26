string_1 = input()
string_2 = input()
"""
print((string_1 in string_2) * "Yes"+ (string_1 not in string_2) * "No")	
"""

is_valid = string_1 in string_2
output = "Yes" if is_valid else "No"
print(output)