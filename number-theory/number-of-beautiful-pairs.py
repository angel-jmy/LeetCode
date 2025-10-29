class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        N = len(nums)
        coprime = {l:[r for r in range(10) if gcd(l, r) == 1] for l in range(10)}
        cache = {} # Record the first digit of every number

        l, r = 0, 0
        counter = 0

        first_last = lambda num: (int(str(num)[0]), int(str(num)[-1]))

        for r in range(N):
            first, last = first_last(nums[r])
            coprimes = coprime[last]
            new_count = 0
            for d in cache:
                if d in coprimes:
                    new_count += cache.get(d, 0)
            counter += new_count
            cache[first] = cache.get(first, 0) + 1

        return counter
