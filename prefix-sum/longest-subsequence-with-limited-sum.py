class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        M = len(queries)
        nums.sort()
        N = len(nums)
        prefs = [0] * N 
        prefs[0] = nums[0]
        for i in range(1, N):
            prefs[i] = prefs[i - 1] + nums[i]
        
        answer = []
        for q in queries:
            idx = bisect_right(prefs, q)
            answer.append(idx)

        return answer