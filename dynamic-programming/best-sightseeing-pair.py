class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)
        curr_part = values[0] + 0
        max_sum = -float('inf')

        for i in range(1, N):
            max_sum = max(max_sum, curr_part + values[i] - i)
            curr_part = max(curr_part, values[i] + i)

        return max_sum

