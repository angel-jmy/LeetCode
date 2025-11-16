class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        M = len(potions)

        for s in spells:
            comp = success / s
            idx = bisect_left(potions, comp)
            res.append(M - idx)

        return res

