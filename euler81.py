
f= open("matrix.txt")
matrix = "],[".join(f.read().split("\n"))[:-2]
matrix = eval("[["+matrix+"]")
f.close()

def column_row_map(col, matrix):
    row=[]
    for i in range(len(matrix)):
        row.append(matrix[i][col])


for i in range(79):
    matrix[0][i+1]+= matrix[0][i]
    matrix[i+1][0] += matrix[i][0]

for row in range(1,80):
    for col in range(1,80):
        top_path = matrix[row - 1][col]
        left_path = matrix[row][col - 1]
        if top_path < left_path:
            matrix[row][col] += top_path
        else:
            matrix[row][col] += left_path

print matrix[-1][-1]
