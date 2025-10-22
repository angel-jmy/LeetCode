class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        last = 0
        for t in target:
            if t - last > 1:
                res.extend(['Push'] * (t - last - 1) + ['Pop'] * (t - last - 1))
            
            last = t
            res.append('Push')
            
        return res
