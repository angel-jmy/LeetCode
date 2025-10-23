class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1 = len(nums1)
        N2 = len(nums2)

        stack = []
        hashmap = {}
        res = []

        for i in range(N2 - 1, -1, -1):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()
            if stack:
                hashmap[nums2[i]] = nums2[stack[-1]]

            stack.append(i)
            

        for num in nums1:
            res.append(hashmap.get(num, -1))

        return res