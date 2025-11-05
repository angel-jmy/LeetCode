class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        N = len(prizePositions)
        
        def single_best(left, right):
            l = left
            best = 0
            for r in range(left, right + 1):
                while prizePositions[r] - prizePositions[l] > k:
                    l += 1
                best = max(best, r - l + 1)

            return best

        largest = 0

        for i in range(N):
            left_best = single_best(0, i)
            right_best = single_best(i + 1, N - 1)
            largest = max(largest, left_best + right_best)

        return largest


