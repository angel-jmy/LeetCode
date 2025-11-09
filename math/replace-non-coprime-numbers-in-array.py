class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if res and gcd(res[-1], num) != 1:
                num0 = res.pop()
                GCD = gcd(num0, num)
                res.append(num0 * num // GCD)
            else:
                res.append(num)

        return res
        
