class Solution:
    def minLength(self, s: str) -> int:
        res = []
        for i in range(len(s)):
            c = s[i]
            if not res:
                res.append(c)
            else:
                if c == 'B' and res[-1] == 'A':
                    res.pop()
                elif c == 'D' and res[-1] == 'C':
                    res.pop()
                else:
                    res.append(c)

        return len(res)