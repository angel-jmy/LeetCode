class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = p3 = p5 = 0
        res = [1] * n
        for i in range(1, n):
            u2, u3, u5 = res[p2] * 2, res[p3] * 3, res[p5] * 5
            res[i] = min(u2, u3, u5)
            if u2 <= u3 and u2 <= u5:
                p2 += 1
            if u3 <= u2 and u3 <= u5:
                p3 += 1
            if u5 <= u2 and u5 <= u3:
                p5 += 1

            # print(p2, p3, p5, res[i])

        return res[n - 1]