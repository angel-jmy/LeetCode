class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(num):
            sum_d = 0
            while num:
                sum_d += num % 10
                num //= 10
            
            return sum_d

        digits = defaultdict(list)
        for num in nums:
            d = sum_digits(num)
            if len(digits[d]) < 2:
                heapq.heappush(digits[d], num)
            else:
                heapq.heappushpop(digits[d], num)
        
        max_sum = -1
        for d in digits.keys():
            if len(digits[d]) < 2:
                continue
            max_sum = max(max_sum, sum(digits[d]))

        return max_sum
