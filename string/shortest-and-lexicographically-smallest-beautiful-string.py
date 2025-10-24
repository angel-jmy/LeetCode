class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        N = len(s)
        l, r = 0, 0
        counts = 0
        min_len = N + 1
        min_str = "1" * (N + 1)

        for r in range(N):
            if s[r] == '1':
                counts += 1

            while counts == k:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_str = s[l:r+1]
                elif r - l + 1 == min_len:
                    min_str = min(min_str, s[l:r+1])
                
                
                if s[l] == '1':
                    counts -= 1
                    l += 1
                else:
                    l += 1
        
        # print(min_len)

        return min_str if min_str != "1" * (N + 1) else ""