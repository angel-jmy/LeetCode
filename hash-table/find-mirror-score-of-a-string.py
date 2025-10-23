class Solution:
    def calculateScore(self, s: str) -> int:
        def get_reverse(c: str) -> str:
            i = ord(c) - ord('a')
            new_i = 25 - i

            return chr(ord('a') + new_i)

        hashmap = defaultdict(list)
        score = 0
        for idx, c in enumerate(s):
            rev = get_reverse(c)
            if rev not in hashmap:
                hashmap[c].append(idx)
            else:
                i = hashmap[rev].pop()
                score += idx - i
                if not hashmap[rev]:
                    del hashmap[rev]
        
        return score
        
            

