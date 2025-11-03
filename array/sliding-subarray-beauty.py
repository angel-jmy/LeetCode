class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        res = [0] * (N - k + 1)

        counts = Counter(nums[:k])
        counter = 0

        for num in range(-50, 0):
            counter += counts[num]
            if counter >= x:
                res[0] = num
                break

        for i in range(1, N - k + 1):
            counts[nums[i - 1]] -=1
            counts[nums[i + k - 1]] += 1
            counter = 0
            # print(counts)
            for num in range(-50, 0):
                counter += counts[num]
                # print(counter, num)
                if counter >= x:
                    res[i] = num
                    break

        return res