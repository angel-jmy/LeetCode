class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        # rewardValues.sort()  
        # ans = {0}  
        # for r in rewardValues:
        #     new_rewards = set()
        #     for x in ans:
        #         if r > x:
        #             new_rewards.add(x + r)
        #     ans.update(new_rewards)
        
        # return max(ans)
        
        rewardValues.sort()                     # process from small to large
        total = sum(rewardValues)

        # dp[s] == True  <=>  total s is reachable
        dp = [False] * (total + 1)
        dp[0] = True
        max_reach = 0                           # largest reachable total so far

        for r in rewardValues:
            # Only totals t < r are allowed to take r; scan t downward to avoid reusing r
            upper = min(max_reach, r - 1)
            for t in range(upper, -1, -1):
                if dp[t]:
                    if not dp[t + r]:
                        dp[t + r] = True
                        if t + r > max_reach:
                            max_reach = t + r

        return max_reach
