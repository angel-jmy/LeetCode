class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
    
        def binary_search(target):
            l, r = 0, N - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        
        print(binary_search(8))

        res = []
        for q in queries:
            idx = binary_search(q)
            print(idx)
            ops = prefs[idx] + suffs[idx]
            res.append(ops)

        return res

