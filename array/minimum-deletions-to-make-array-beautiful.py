class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = []
        cur_len = 0
        removed = 0

        for i in range(len(nums)):
            num = nums[i]
            if not res:
                res.append(num)
                cur_len += 1
            else:
                if cur_len % 2 == 1 and num == res[-1]:
                    removed += 1
                else:
                    res.append(num)
                    cur_len += 1

        return removed if cur_len % 2 == 0 else removed + 1            
            