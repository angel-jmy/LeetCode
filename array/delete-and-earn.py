class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        m = max(cnt)  # max value present
        pts = [0] * (m + 1)
        for v, c in cnt.items():
            pts[v] = v * c

        prev2, prev1 = 0, pts[1]   # house robber DP
        for i in range(2, m + 1):
            cur = max(prev1, prev2 + pts[i])
            prev2, prev1 = prev1, cur
        return prev1