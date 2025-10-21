class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            for j in range(y, y + k):
                c1 = x + i
                c2 = x + k - i - 1
                grid[c1][j], grid[c2][j] = grid[c2][j], grid[c1][j]

        return grid