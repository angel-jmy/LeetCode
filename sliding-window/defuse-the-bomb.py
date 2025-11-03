class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        if k > 0:
            code2 = code + code[:k]
            N = len(code)
            res = [0] * N
            res[N - 1] = sum(code2[N:N + k])
            for i in range(N - 2, -1, -1):
                res[i] = res[i + 1] - code2[i + k + 1]
                res[i] += code2[i + 1]

        else:
            k = -k
            code2 = code[-k:] + code
            N = len(code)
            res = [0] * N
            res[0] = sum(code2[:k])
            for i in range(1, N):
                res[i] = res[i - 1] - code2[i - 1]
                res[i] += code2[i + k - 1]

        return res
