class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        N = len(s)
        mapping = {}
        mapped = set()
        for i in range(N):
            c1, c2 = s[i], t[i]
            if c1 not in mapping:
                if c2 in mapped:
                    return False
                    
                mapping[c1] = c2
                mapped.add(c2)
            else:
                if mapping[c1] != c2:
                    return False

        return True