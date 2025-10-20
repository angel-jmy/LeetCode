class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        op = 0
        for num in nums:
            if num > k:
                continue
            comp = k - num
            if comp in counts:
                counts[comp] -= 1
                op += 1
                if counts[comp] == 0:
                    del counts[comp]
            else:
                counts[num] += 1

        return op