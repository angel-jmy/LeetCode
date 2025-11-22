class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def sum_div(div):
            divided = [ceil(num / div) for num in nums]
            return sum(divided)

        l, r = 1, max(nums) + 1
        while l <= r:
            mid = l + (r - l) // 2
            result = sum_div(mid)
            if result > threshold:
                l = mid + 1
            else:
                r = mid - 1
        return l