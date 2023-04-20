class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i] = matrix[i][::-1]
