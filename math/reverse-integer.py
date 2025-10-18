class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = 1 if x > 0 else -1
        x = abs(x)
        num = 0

        while x > 0:
            num = 10 * num + x % 10
            x = x // 10

        if sign * num < -2 ** 31 or sign * num > 2 ** 31 - 1:
            return 0

        return sign * num 

