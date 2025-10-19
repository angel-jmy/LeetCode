class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        largest = -1
        for num in nums:
            if num not in seen and -num not in seen:
                seen.add(num)
            elif num not in seen and -num in seen:
                seen.add(num)
                largest = max(largest, abs(num))


        return largest