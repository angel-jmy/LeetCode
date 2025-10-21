class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l, r = 0, N - 1

        res = deque()
        while l < r:
            l_sq, r_sq = nums[l] ** 2, nums[r] ** 2
            if l_sq > r_sq:
                res.appendleft(l_sq)
                l += 1
            else:
                res.appendleft(r_sq)
                r -= 1

        res.appendleft(nums[l] ** 2)

        return list(res)