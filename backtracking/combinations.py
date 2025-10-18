class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, k0):
            if k0 == k:
                res.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path, k0 + 1)
                path.pop()

        backtrack(1, [], 0)

        return res


