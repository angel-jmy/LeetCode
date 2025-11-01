class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        M = len(potions)
        # spells.sort()
        potions.sort()

        res = []
        for s in spells:
            comp = success / s
            i = bisect_left(potions, comp)
            res.append(M - i)

        return res

