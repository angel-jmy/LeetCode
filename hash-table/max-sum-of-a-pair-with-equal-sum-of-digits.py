class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(n):
            res = 0
            while n:
                res += n % 10
                n //= 10

            return res

        cache = {}
        curr = -1
        for num in nums:
            val = sum_digits(num)
            if val in cache:
                curr = max(curr, cache[val] + num)
                cache[val] = max(cache[val], num)

            else:
                cache[val] = num

        return curr