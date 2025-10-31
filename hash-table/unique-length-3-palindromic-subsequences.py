class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        before = set(s[:1])
        after = Counter(s[2:])
        
        res = set()
        for j in range(1, N - 1):

            for char in range(ord('a'), ord('z') + 1):
                c = chr(char)
                if c in before and after[c] > 0:
                    res.add((c, s[j], c))
            
            before.add(s[j])
            after[s[j + 1]] -= 1
            
        return len(res)

                