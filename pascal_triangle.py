# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

# # Variation 1: Print element at given row,col in pascal's triangle
# def nCr(n, row):
#     res = 1

#     for i in range(row):
#         res = res * (n-i)
#         res = res / (i+1)
#     return res

# def pascal_triangle(row, col):
#     elem = nCr(row-1, col-1)
#     return elem

# def main():
#     row = 5
#     col = 3
#     result = pascal_triangle(row, col)
#     print(f"element at position {(row, col)} = {result}")

# if __name__ == "__main__":
#     main()

# # Variation 2: Print nth row in pascal's triangle
## Time complexity: O(N), Space complexity: O(1)
# n = 6
# ans = 1
# print(ans, end=" ")
# for i in range(1, n):
#     ans = ans * (n-i)
#     ans = ans // i
#     print(ans, end=" ")
# print(" ")

# # Variation 3: Print pascal's triangle for given number of rows = n
# # Time Complexity = O(N^2), Space Complexity = O(1) 
def getRows(row):
    ans = 1
    ansRow = [1] # Insert first element

    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        ansRow.append(ans)
    return ansRow

def Pascal_triangle(n: int) -> list[list[int]]:
    ans = []
    for row in range(1, n+1):
        ans.append(getRows(row))
    return ans

def main():
    n = 5
    result = Pascal_triangle(n)
    print(f"Pascal's Triangle for n = {n} is: ")
    for item in result:
        for i in item:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    main()