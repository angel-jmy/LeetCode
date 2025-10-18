class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        left = {}
        right = {}
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            if num not in left:
                left[num] = i
            right[num] = i
        degree = max(count.values())
        res = float('inf')
        for num in count:
            if count[num] == degree:
                res = min(res, right[num] - left[num] + 1)
        return res
