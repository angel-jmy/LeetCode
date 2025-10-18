class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        islands = 0

        def dfs(x, y):
            visit[x][y] = True
            if x - 1 >= 0 and not visit[x - 1][y]:
                if grid[x - 1][y] == '1':
                    dfs(x - 1, y)
            if x + 1 < m and not visit[x + 1][y]:
                if grid[x + 1][y] == '1':
                    dfs(x + 1, y)
            if y - 1 >= 0 and not visit[x][y - 1]:
                if grid[x][y - 1] == '1':
                   dfs(x, y - 1)
            if y + 1 < n and not visit[x][y + 1]:
                if grid[x][y + 1] == '1':
                    dfs(x, y + 1)


        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        
        return islands