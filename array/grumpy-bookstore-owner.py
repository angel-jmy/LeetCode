class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        total = sum(customers)
        window = [-1, -1]
        max_num = 0
        curr_num = 0
        l = 0

        for r in range(N):
            curr_num += customers[r]
            if r - minutes + 1 > 0:
                l = r - minutes
                curr_num -= customers[l]
                l += 1

            if curr_num > max_num:
                max_num = curr_num
                window = [l, r]

        rest = sum([customers[i] * (1 - grumpy[i]) for i in range(N) if i < window[0] or i > window[1]])
        print(window)
        print(rest)

        return rest + max_num

