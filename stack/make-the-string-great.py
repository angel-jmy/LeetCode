class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            c = s[i]
            if not res:
                res.append(c)
            else:
                if c != res[-1] and (c.lower() == res[-1] or c.upper() == res[-1]):
                    res.pop()
                else:
                    res.append(c)

        return ''.join(res)