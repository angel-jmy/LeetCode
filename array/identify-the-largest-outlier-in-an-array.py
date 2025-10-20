class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = 0
        hashmap = defaultdict(int)
        for num in nums:
            total += num
            hashmap[num] += 1
        
        max_out = -float('inf')
        keys = hashmap.keys()
        for num in list(keys):
            if (total - num) % 2: 
                continue
            
            comp = (total - num) // 2
            if (hashmap[comp] and num != comp) or (hashmap[comp] > 1 and num == comp):
                max_out = max(max_out, num)

        return max_out
