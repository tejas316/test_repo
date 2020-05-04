import re
rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))
matrix = []
for i in range(rows):
    elements = []
    for j in range(columns):
        elements.append(input())
    matrix.append(elements)

# For printing the matrix
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
    
# For printing the string
string = ""
for y in range(columns):
    for x in range(rows):
        string += matrix[x][y]
temp_len = len(string) - len(re.sub(r'\W+', ' ', string))
string = re.sub(r'\W+', ' ', string[:-temp_len]) + string[-temp_len:]
print(string)
