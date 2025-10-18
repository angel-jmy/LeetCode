class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        nums = []
        if len(count1) < len(count2):
            for num in count1:
                if num in count2:
                    nums.append(num)
        else:
            for num in count2:
                if num in count1:
                    nums.append(num)

        return nums