class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        cache = defaultdict(int)
        cache[0] = 1
        curr_sum = 0
        counter = 0

        for i in range(N):
            curr_sum += arr[i]
            if curr_sum % 2:
                counter += cache[0]
                cache[1] += 1
            else:
                counter += cache[1]
                cache[0] += 1

        return counter % MOD


