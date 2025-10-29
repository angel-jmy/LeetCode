class Solution:
    def similarPairs(self, words: List[str]) -> int:
        N = len(words)
        hashmap = defaultdict(int)
        counter = 0

        for r in range(N):
            counts = Counter(words[r])
            uniques = tuple(sorted(list(counts.keys())))
            counter += hashmap[uniques]
            hashmap[uniques] += 1

        return counter
