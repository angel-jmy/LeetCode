class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]
        N = len(startTime)
        curr_gap = 0
        max_gap = 0

        for i in range(1, N):
            curr_gap += startTime[i] - endTime[i - 1]
            left = i - k - 1
            if left > 0:
                curr_gap -= startTime[left] - endTime[left - 1]

            max_gap = max(max_gap, curr_gap)

        return max_gap


