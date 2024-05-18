string = input()
if "." in string:
    indx = string.index(".")
    print(string[indx+1])
else:
    print(0)