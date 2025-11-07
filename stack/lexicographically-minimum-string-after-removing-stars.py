class Solution:
    def clearStars(self, s: str) -> str:
        N = len(s)
        pos = [[] for _ in range(26)]
        counts = [0] * 26
        tot_len = 0

        for i in range(N):
            c = s[i]
            if c != '*':
                index = ord(c) - ord('a')
                pos[index].append(i)
                counts[index] += 1
                tot_len += 1
            else:
                for j in range(26):
                    char = chr(j + ord('a'))
                    if pos[j]:
                        pos[j].pop()
                        tot_len -= 1
                        counts[j] -= 1
                        break

        print(tot_len)
        print(pos)
        res = ['0'] * tot_len

        for i in range(26):
            char = chr(i + ord('a'))
            print(pos[i])
            if pos[i]:
                for idx in pos[i]:
                    res[idx] = char

        return "".join(res)

