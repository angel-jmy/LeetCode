class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, cur_sum = 0, 0
        cache = {0:1}

        for num in nums:
            cur_sum += num
            count += cache.get(cur_sum - k, 0)
            cache[cur_sum] = cache.get(cur_sum, 0) + 1
  
        return count