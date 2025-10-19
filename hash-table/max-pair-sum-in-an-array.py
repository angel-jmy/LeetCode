class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def largest(num: int) -> int:
            max_digit = 0
            while num:
                max_digit = max(max_digit, num % 10)
                num //= 10
            
            return max_digit

        max_d = 0
        max_list = []

        for num in nums:
            d = largest(num)
            if d > max_d:
                max_d = d
                max_list = [-num]
            elif d == max_d:
                heapq.heappush(max_list, -num)
        
        if len(max_list) < 2:
            return -1

        max_sum = 0
        for _ in range(2):
            max_sum += -heapq.heappop(max_list)

        return max_sum