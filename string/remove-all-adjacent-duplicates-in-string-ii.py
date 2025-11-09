class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        cur_len = 0

        for i in range(len(s)):
            c = s[i]
            if not res:
                res.append(c)
                cur_len += 1
            else:
                if cur_len >= k - 1:
                    for j in range(1, k):
                        if res[cur_len - j] != c:
                            res.append(c)
                            cur_len += 1
                            break
                    else:
                        for _ in range(1, k):
                            res.pop()
                            cur_len -= 1
                else:
                    res.append(c)
                    cur_len += 1
            

        return ''.join(res)