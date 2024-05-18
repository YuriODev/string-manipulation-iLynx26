collumn_1 = int(input())
collumn_2 = int(input())+1
row_1 = int(input())
row_2 = int(input())

output_1 = "\t"
for i in range(row_1, row_2+1):
    output_1 += f"{i}\t"

print(output_1)
for i in range(collumn_1, collumn_2):
    output = f"{i}\t"
    for j in range(row_1, row_2+1):
        output += f"{j*i}\t"
    print(output)