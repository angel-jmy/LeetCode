class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for i in range(32):
            bit = n & 1
            counter += bit
            n >>= 1

        return counter