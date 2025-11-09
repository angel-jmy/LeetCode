class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        counts = defaultdict(int)
        cur_len = 0


        for i in range(len(s)):
            c = s[i]
            res.append(c)
            counts[c] += 1
            if counts[c] == k:
                res = res[:-k]
                counts[c] -= k

        return ''.join(res)
