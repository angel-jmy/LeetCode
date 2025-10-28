class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        cache = {0:1}
        curr_sum = 0
        counter = 0

        for i in range(N):
            curr_sum += arr[i]
            if curr_sum % 2:
                counter = (counter + cache.get(0, 0)) % MOD
                cache[1] = cache.get(1, 0) + 1
            else:
                counter = (counter + cache.get(1, 0)) % MOD
                cache[0] = cache.get(0, 0) + 1

        return counter


