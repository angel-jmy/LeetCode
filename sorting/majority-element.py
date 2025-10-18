class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        hashmap = {}

        for elem in nums:
            hashmap[elem] = hashmap.get(elem, 0) + 1
            if hashmap[elem] > N // 2:
                return elem