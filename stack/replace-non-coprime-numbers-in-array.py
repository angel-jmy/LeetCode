class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)
        i = 0
        last_merge = False
        while i < N:
            if last_merge:
                num = to_merge
            else:
                num = nums[i]

            if res and gcd(res[-1], num) != 1:
                num0 = res.pop()
                GCD = gcd(num0, num)
                to_merge = num0 * num // GCD
                last_merge = True
            else:
                res.append(num)
                last_merge = False
                i += 1

        return res

