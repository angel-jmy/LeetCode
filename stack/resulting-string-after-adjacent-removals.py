class Solution:
    def resultingString(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            c = s[i]
            if not res:
                res.append(c)
            else:
                diff = abs(ord(c) - ord(res[-1]))
                if diff == 1 or diff == 25:
                    res.pop()
                else:
                    res.append(c)

        return ''.join(res)