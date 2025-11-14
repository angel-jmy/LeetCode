class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[0] * (r + 1) for r in range(rowIndex + 1)]

        for r in range(rowIndex + 1):
            for i in range(r + 1):
                if i == 0 or i == r:
                    triangle[r][i] = 1
                else:
                    triangle[r][i] = triangle[r - 1][i - 1] + triangle[r - 1][i]

        return triangle[rowIndex]

