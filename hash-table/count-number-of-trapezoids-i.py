class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        # Couter of lines using y axes
        counts = defaultdict(int)
        for x, y in points:
            counts[y] += 1

        line_sum = 0 # Number of lines
        sq_sum = 0 # Sum N_lines^2
        for y in counts:
            n = counts[y]
            n_lines = n * (n - 1) // 2
            line_sum += n_lines
            sq_sum += n_lines ** 2
   

        return (line_sum ** 2 -sq_sum) // 2 # Formula!!!