class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def best(L, M):
            # Max sum where an L-length window occurs before an M-length window
            n = len(nums)
            # initial window sums
            Lsum = sum(nums[:L])
            Msum = sum(nums[L:L+M])
            maxL = Lsum
            ans = maxL + Msum

            # i indexes the *end* of the combined prefix we’ve scanned so far.
            # At each step, we advance both windows by 1:
            #   - L window ends at i-M (so its start is i-M-L+1)
            #   - M window ends at i   (start is i-M+1)
            for i in range(L + M, n):
                # advance L window by 1: drop nums[i-M-L], add nums[i-M]
                Lsum += nums[i - M] - nums[i - M - L]
                maxL = max(maxL, Lsum)

                # advance M window by 1: drop nums[i-M], add nums[i]
                Msum += nums[i] - nums[i - M]

                ans = max(ans, maxL + Msum)
            return ans

        return max(best(firstLen, secondLen), best(secondLen, firstLen))