class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        window = [-1, -1]
        max_add = 0
        curr_num = 0
        l = 0

        for r in range(N):
            curr_num += customers[r] * grumpy[r]
            if r - minutes + 1 > 0:
                l = r - minutes
                curr_num -= customers[l] * grumpy[l]
                l += 1

            if curr_num > max_add:
                max_add = curr_num
                window = [l, r]

        total = sum([customers[i] * (1 - grumpy[i]) for i in range(N)])
        print(window)
        print(max_add)


        return total + max_add

