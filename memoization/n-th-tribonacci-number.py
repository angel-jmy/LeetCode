class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        ppprev, pprev, prev = 0, 1, 1
        curr = 0

        for idx in range(3, n + 1):
            curr = ppprev + pprev + prev
            ppprev = pprev
            pprev = prev
            prev = curr

        return curr