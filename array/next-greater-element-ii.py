class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums2 = nums * 2
        res = [-1] * N
        stack = []

        for i in range(2 * N - 1, -1, -1):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()
            if stack:
                idx = i - N if i > N - 1 else i
                if res[idx] == -1:
                    res[idx] = nums2[stack[-1]]

            stack.append(i)

        return res