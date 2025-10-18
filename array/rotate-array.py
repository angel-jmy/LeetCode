class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        N = len(nums)
        k = k % N
        numsk = nums[N-k:]
        nums0 = nums[:N-k]
        
        for i in range(N-k):
            nums[i + k] = nums0[i]
            
        for i in range(k):
            nums[i] = numsk[i]
            
        