class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counts2 = Counter(words2[0])
        for w in words2[1:]:
            newcount = Counter(w)
            for c in newcount:
                if c in counts2:
                    counts2[c] = max(counts2[c], newcount[c])
                else:
                    counts2[c] = newcount[c]
            # counts2 += newcount

        res = []

        for w in words1:
            counts = Counter(w)
            for c in counts2:
                if c not in counts:
                    break
                elif counts2[c] > counts[c]:
                    break
            else:
                res.append(w)

        return res