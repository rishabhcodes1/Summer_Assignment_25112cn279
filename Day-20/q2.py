
n = int(input("Enter size of matrix: "))

matrix = []

print("Enter matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False

if flag:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")