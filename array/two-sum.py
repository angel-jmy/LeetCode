class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap:
                return [hashmap[comp], i]
            else:
                hashmap[nums[i]] = i
                
                    