class NumArray:

    def __init__(self, nums: List[int]):
        # self.numlist = nums
        N = len(nums)
        self.prefs = [0] * (N + 1)
        for i in range(1, N + 1):
            self.prefs[i] = self.prefs[i - 1] + nums[i - 1]



    def sumRange(self, left: int, right: int) -> int:
        return self.prefs[right + 1] - self.prefs[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)