class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curr_idx = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue
              
            nums[curr_idx] = nums[i]
            curr_idx += 1

        return curr_idx