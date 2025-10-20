class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        # Couter of points and lines using y axes
        counts = defaultdict(int)
        lines = defaultdict(int)
        for x, y in points:
            lines[y] += counts[y]
            counts[y] += 1

        ylist = list(lines.keys())
        N_y = len(ylist)

        total = 0
        for i in range(N_y):
            for j in range(i + 1, N_y):
                total = (total + lines[ylist[i]] * lines[ylist[j]]) % MOD

        return total