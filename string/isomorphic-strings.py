class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        N = len(s)
        mapping = {}
        for i in range(N):
            c1, c2 = s[i], t[i]
            if c1 not in mapping:
                mapping[c1] = c2
            else:
                if mapping[c1] != c2:
                    return False

        return True