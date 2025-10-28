class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        N = len(nums)
        indexes = [i for i in range(N) if nums[i] == 0]

        def isValid(idx, dir_, arr, cur_sub):
            if cur_sub == total:
                return True
            if idx < 0:
                return False
            if idx > N - 1:
                return False
            if arr[idx] > 0:
                newarr = arr[:]
                newarr[idx] -= 1
                return isValid(idx - dir_, -dir_, newarr, cur_sub + 1)

            else:
                newarr = arr[:]
                return isValid(idx + dir_, dir_, newarr, cur_sub)

        res = 0
        for idx in indexes:
            if isValid(idx, 1, nums[:], 0):
                res += 1
            if isValid(idx, -1, nums[:], 0):
                res += 1

        return res
                
