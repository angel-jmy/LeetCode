class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        all_num = set()
        for num in nums:
            if -num in all_num:
                res = max(res, abs(num))

            all_num.add(num)

        return res