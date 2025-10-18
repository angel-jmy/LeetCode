class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rottens = deque()
        fresh = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottens.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        steps = 0

        while rottens:
            size = len(rottens)
            advanced = False

            for _ in range(size):
                rot = rottens.popleft()

                for d in dirs:
                    newi, newj = rot[0] + d[0], rot[1] + d[1]
                    if 0 <= newi < m and 0 <= newj < n:
                        if grid[newi][newj] == 1:
                            grid[newi][newj] = 2
                            fresh -= 1
                            advanced = True
                            rottens.append([newi, newj])

            if advanced == True:
                steps += 1
                

        return steps if fresh == 0 else -1

