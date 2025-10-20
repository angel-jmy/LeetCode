class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mods = {}
        pairs = 0
        self_pairs = 0
        for t in time:
            curr_mod = t % 60
            if curr_mod == 0:
                self_pairs += 1
                continue
            comp = 60 - curr_mod
            if comp in mods:
                pairs += mods[comp]

            mods[curr_mod] = mods.get(curr_mod, 0) + 1

        pairs += self_pairs * (self_pairs - 1) // 2

        return pairs
            