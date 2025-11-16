class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        N = len(nums)
        def find_neg():
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < 0:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def find_pos():
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > 0:
                    r = mid - 1
                else:
                    l = mid + 1
            return N - r - 1

        neg, pos = find_neg(), find_pos()

        return max(neg, pos)