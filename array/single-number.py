class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        
        seen = {}
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        for num in nums:
            if seen[num] == 1:
                return num
        
        
        