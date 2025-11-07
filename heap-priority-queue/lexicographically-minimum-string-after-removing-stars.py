class Solution:
    def clearStars(self, s: str) -> str:
        N = len(s)
        pos = [[] for _ in range(26)]
        # counts = [0] * 26
        # tot_len = 0
        deleted = set()

        for i in range(N):
            c = s[i]
            if c != '*':
                index = ord(c) - ord('a')
                pos[index].append(i)

            else:
                for j in range(26):
                    char = chr(j + ord('a'))
                    if pos[j]:
                        idx = pos[j].pop()
                        deleted.add(idx)
                        break

        res = []

        for i in range(N):
            if s[i] != '*' and i not in deleted:
                res.append(s[i])

        return "".join(res)

