class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = n & 1
            res = res * 2 + bit
            n >>= 1

        return res