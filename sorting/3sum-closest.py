class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        N = len(nums)
        min_diff = float('inf')
        minus = False

        for i in range(N - 2):
            l, r = i + 1, N - 1

            while l < r:
                _sum = nums[i] + nums[l] + nums[r]

                diff = _sum - target
                

                if diff == 0:
                    return target

                if diff < 0:
                    if -diff >= min_diff:
                        l += 1
                        continue

                    min_diff = min(min_diff, -diff)
                    minus = True
                    l += 1

                else:
                    if diff >= min_diff:
                        r -= 1
                        continue

                    min_diff = min(min_diff, diff)
                    minus = False
                    r -= 1
            
        return target + min_diff * (-1 if minus else 1)