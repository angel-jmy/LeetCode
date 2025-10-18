class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(start, remain, path):
            if remain == 0:
                res.append(path[:])  # copy
                return

            for i in range(start, n):
                # skip duplicates at the same depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # pruning
                if candidates[i] > remain:
                    break
                # choose
                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], path)  # i+1: use once
                path.pop()  # un-choose

        backtrack(0, target, [])
        return res

