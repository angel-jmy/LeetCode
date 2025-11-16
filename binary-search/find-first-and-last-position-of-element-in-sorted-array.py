class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        def find_left():
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r + 1

        def find_right():
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l - 1

        left = find_left()
        right = find_right()

        return [left, right] if left <= right else [-1, -1]