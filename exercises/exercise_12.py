number = int(input())

str_1 = "   _~_   "
str_2 = "  (o o)  "
str_3 = " /  V  \ "
str_4_1 = "/(  "
str_4_2 = "  )\\"
str_5 = "  ^^ ^^  "

actual_str_1 = ""
actual_str_2 = ""
actual_str_3 = ""
actual_str_4 = ""
actual_str_5 = ""

for i in range(number):
    actual_str_1 += str_1 + "     "
    actual_str_2 += str_2 + "     "
    actual_str_3 += str_3 + "     "
    actual_str_4 += str_4_1 + str(i+1) + str_4_2 + "     "
    actual_str_5 += str_5 + "     "

print(actual_str_1.rstrip())
print(actual_str_2.rstrip())
print(actual_str_3.rstrip())
print(actual_str_4.rstrip())
print(actual_str_5.rstrip())
