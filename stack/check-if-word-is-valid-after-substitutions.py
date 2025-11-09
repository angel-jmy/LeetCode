class Solution:
    def isValid(self, s: str) -> bool:
        t = []
        for i in range(len(s)):
            c = s[i]
            if not t and c != 'a':
                return False

            if c != 'c':
                t.append(c)

            elif c == 'c' and (not t or not t[:-1]):
                return False

            elif c == 'c' and t and t[:-1]:
                if t[-1] != 'b' or t[-2] != 'a':
                    return False
                else:
                    t.pop()
                    t.pop()
            
            else:
                t.append(c)

        return not t