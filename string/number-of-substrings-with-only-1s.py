class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)
        l = 0
        # cur_len = 0
        counter = 0
        for r in range(N):
            if s[r] == '0':
                if r > 0 and s[r - 1] == '1':
                    n = r - l
                    counter = (counter + n * (n + 1) // 2) % MOD
                l = r + 1
        
        # print(l, r)
        if s[r] == '1':
            n = r - l + 1
            counter = (counter + n * (n + 1) // 2) % MOD

        return counter