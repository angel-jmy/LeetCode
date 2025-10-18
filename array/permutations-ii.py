class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def backtrack(path, remains):
            if not remains:
                res.append(path[:])
                return

            for i in range(len(remains)):
                if i > 0 and remains[i] == remains[i - 1]:
                    continue

                path.append(remains[i])
                backtrack(path, remains[:i] + remains[i + 1:])
                path.pop()

        backtrack([], nums)

        return res