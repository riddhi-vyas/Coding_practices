# Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
# Examples 1:
# Input:
#  matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output:
#  [[1,0,1],[0,0,0],[1,0,1]]

# Explanation:
#  Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

# Brute Force Approach:
# Time Comp: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix
# Space Comp: O(1)

def mark_Row(matrix, n, m, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def mark_Col(matrix, n, m, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zero_Matrix(matrix, n, m):
    # replace non-zero items with -1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                mark_Row(matrix, n, m, i)
                mark_Col(matrix, n, m, j)
    # replace items having -1 with 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

def main():
    # matrix: List[List[int]]
    matrix=[[1,1,1],[1,0,1],[1,1,1]]
    m = len(matrix)
    n = len(matrix[0])
    # print(f"#Rows = {m}, #Cols = {n}")
    ans = zero_Matrix(matrix, n, m)
    print(f"Matrix: {matrix}")

if __name__ == "__main__":
    main()


        
