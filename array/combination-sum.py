class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []   
        candidates.sort()
        global size
        size = 0
        N = len(candidates)

        def backtrack(start, remain, path):
            global size
            if remain == 0:
                if size + 1 > 150:
                    return
                size += 1
                res.append(path[:])
                return

            for i in range(start, N):
                if candidates[i] > remain:
                    break
                
                path.append(candidates[i])
                backtrack(i, remain - candidates[i], path)
                path.pop()

                # path.append(candidates[i])
                # backtrack(i + 1, remain - candidates[i], path)
                # path.pop()

        
        backtrack(0, target, [])

        return res