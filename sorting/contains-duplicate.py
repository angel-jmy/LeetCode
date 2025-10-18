class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        allseen = {}
        for num in nums:
            if num in allseen:
                return True
            allseen[num] = 1

        return False
        