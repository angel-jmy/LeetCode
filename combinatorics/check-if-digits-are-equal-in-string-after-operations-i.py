class Solution:
    def hasSameDigits(self, s: str) -> bool:
        N = len(s)
        
        while N > 2:
            s1 = []
            for i in range(N - 1):
                s1.append(str((int(s[i]) + int(s[i + 1])) % 10))

            s = ''.join(s1)
            N -= 1

        return s[0] == s[1]
        
