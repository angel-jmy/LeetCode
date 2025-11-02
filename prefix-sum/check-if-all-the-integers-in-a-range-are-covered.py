class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key = lambda x: (x[0], x[1]))
        N = len(ranges)
        i = 0
        
        for num in range(left, right + 1):
            while num > ranges[i][1] and i + 1 < N:
                i += 1

            if ranges[i][0] <= num <= ranges[i][1]:
                continue
            else:
                return False

        return True