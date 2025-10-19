class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = 0
        hashmap = {}
        for p in dominoes:
            tp = tuple(sorted(p))
            if tp in hashmap:
                pairs += hashmap[tp]
            
            hashmap[tp] = hashmap.get(tp, 0) + 1

        return pairs