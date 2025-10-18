class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        p1 = m - 1  # pointer for nums1
        p2 = n - 1  # pointer for nums2
        p = m + n - 1  # pointer for placement in nums1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Copy remaining nums2 elements (if any)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1