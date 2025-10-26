class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        N = len(words)
        pref = [0] * (N + 1)
        for i in range(N):
            w = words[i]
            flag = w[0] in vowels and w[-1] in vowels
            pref[i + 1] = pref[i] + flag

        res = []
        for l, r in queries:
            res.append(pref[r + 1] - pref[l])

        return res