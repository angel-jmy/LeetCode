class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
    
        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for j in range(size // 2):
            for i in range(size):
                matrix[i][j], matrix[i][size - j - 1] = matrix[i][size - j - 1], matrix[i][j]