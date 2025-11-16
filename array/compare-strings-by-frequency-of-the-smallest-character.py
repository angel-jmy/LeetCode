class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:  
        def f(s):
            counts = Counter(s).items()
            return min(counts, key = lambda x: x[0])[1]

        wordsF = [f(w) for w in words]
        wordsF.sort()
        N = len(wordsF)

        res = []
        for q in queries:
            idx = bisect_right(wordsF, f(q))
            res.append(N - idx)

        return res