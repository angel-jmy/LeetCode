class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, k0, remain):
            if k0 == k and remain > 0:
                return

            if remain == 0 and k0 < k:
                return

            if remain == 0 and k0 == k:
                res.append(path[:])
                return

            for num in range(start, 10):
                if num > remain:
                    break

                path.append(num)
                backtrack(num + 1, path, k0 + 1, remain - num)
                path.pop()


        backtrack(1, [], 0, n)

        return res

        