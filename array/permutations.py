class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # if len(nums) == 1:
        #     return [nums[:]]
        
        # res = []

        # for _ in range(len(nums)):
        #     n = nums.pop(0)
        #     perms = self.permute(nums)

        #     for p in perms:
        #         p.append(n)
            
        #     res.extend(perms)
        #     nums.append(n)
        
        # return res

        res = []

        def backtrack(path, remains):
            if not remains:
                res.append(path[:])
                return

            for i in range(len(remains)):
                path.append(remains[i])
                backtrack(path, remains[:i] + remains[i + 1:])
                path.pop()

        backtrack([], nums)

        return res
            