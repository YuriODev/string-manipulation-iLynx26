string = input()

first_index = string.index("\\")
print(string[0:first_index])
second_index = len(string) - string[::-1].index("\\")
print(string[first_index+1:second_index-1])
print(string[second_index:])