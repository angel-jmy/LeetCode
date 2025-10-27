class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        N = len(s)
        nextpref, prevpref = [0] * 53, [0] * 53
        for i in range(52):
            nextpref[i + 1] = nextpref[i] + nextCost[i % 26]
            prevpref[i + 1] = prevpref[i] + previousCost[i % 26]

        tot_cost = 0
        for i in range(N):
            sa, st = s[i], t[i]
            start_idx = ord(sa) - ord('a')
            diff = ord(st) - ord(sa)

            d_fwd = diff % 26
            d_bwd = (-diff) % 26

            n_cost = nextpref[start_idx + d_fwd] - nextpref[start_idx]
            anchor = start_idx + 26
            L = anchor - d_bwd + 1
            R = anchor + 1
            p_cost = prevpref[R] - prevpref[L]

            # print(i, nextdiff, next_idx, prevdiff, prev_idx)

            tot_cost += min(n_cost, p_cost)

        return tot_cost
            