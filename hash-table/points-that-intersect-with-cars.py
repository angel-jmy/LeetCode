class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0][1] - nums[0][0] + 1
        
        nums.sort(key = lambda x: (x[0], x[1]))
        cur_set = set(range(nums[0][0], nums[0][1] + 1))
        counter = nums[0][1] + 1 - nums[0][0]
        # print(cur_set)

        # overlaps = set()
        for i in range(1, N):
            new_count = nums[i][1] + 1 - nums[i][0]
            new_set = set(range(nums[i][0], nums[i][1] + 1))
            # print(new_set)

            overlaps = nums[i - 1][1] - nums[i][0] + 1 if nums[i - 1][1] >= nums[i][0] else 0
            # print(overlaps)
            counter += new_count - overlaps
            cur_set |= new_set
            print(cur_set)

        return counter
