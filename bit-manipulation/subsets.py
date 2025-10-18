class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        # N = len(nums)

        # def backtrack(idx, path, k0, k):
        #     if k0 == k:
        #         res.append(path[:])
        #         return

        #     for i in range(idx, N):
        #         path.append(nums[i])
        #         backtrack(i + 1, path, k0 + 1, k)
        #         path.pop()


        # for k in range(N + 1):
        #     backtrack(0, [], 0, k)
                  

        # return res

        res = []
        
        def create_subset(path, i):
            if i == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            create_subset(path, i+1)

            path.pop()
            create_subset(path, i+1)

        create_subset([], 0)

        return res