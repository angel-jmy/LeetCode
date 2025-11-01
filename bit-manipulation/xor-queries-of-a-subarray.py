class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        prefs = [0] * (N + 1)

        for i in range(N):
            prefs[i + 1] = prefs[i] ^ arr[i]

        res = []
        for q in queries:
            l, r = q
            res.append(prefs[r + 1] ^ prefs[l])

        return res