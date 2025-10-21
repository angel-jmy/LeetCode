class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        l, r = 0, N - 1
        deleted = 0
        while l < r:
            if s[l] == s[r]:
                while l + 1 < r and s[l] == s[l + 1]:
                    deleted += 1
                    l += 1
                while r - 1 > l and s[r] == s[r - 1]:
                    deleted += 1
                    r -= 1
                
                deleted += 2
                l += 1
                r -= 1
            
            else:
                break

        return N - deleted