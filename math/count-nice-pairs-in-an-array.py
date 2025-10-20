class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def rev(num):
            res = 0
            while num:
                res = 10 * res + num % 10
                num //= 10
            
            return res

        counts = {}
        for num in nums:
            val = num - rev(num)
            counts[val] = counts.get(val, 0) + 1
        
        pairs = 0
        for val in counts.keys():
            n = counts[val]
            pairs = (pairs + n * (n - 1) // 2) % MOD

        return pairs
        