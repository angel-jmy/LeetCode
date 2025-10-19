class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # nums.sort(reverse = True)

        def largest(num: int) -> int:
            max_digit = 0
            while num:
                max_digit = max(max_digit, num % 10)
                num //= 10
            
            return max_digit

        digits = defaultdict(list)

        for num in nums:
            d = largest(num)
            heapq.heappush(digits[d], -num)

        max_sum = -1
        for d in digits.keys():
            if len(digits[d]) < 2:
                continue
            cur_sum = 0
            for _ in range(2):
                cur_sum += -heapq.heappop(digits[d])
            
            max_sum = max(max_sum, cur_sum)
    
        return max_sum