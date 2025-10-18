class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        res = {(0, 0):0}
        max_len = 0
        for s in strs:
            c = Counter(s)
            c0, c1 = c.get('0', 0), c.get('1', 0)
            new_res = res.copy()
            for (s0, s1), v in new_res.items():
                if c0 + s0 > m or c1 + s1 > n:
                    continue
                res[(c0 + s0, c1 + s1)] = max(res.get((c0 + s0, c1 + s1), 0), new_res[(s0, s1)] + 1)
                max_len = max(max_len, res[(c0 + s0, c1 + s1)])

        return max_len

        
     