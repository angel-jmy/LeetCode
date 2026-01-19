class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
            
        digits = 0
        while digits != 1:
            digits = 0
            res = 0
            while num:
                res += num % 10
                num //= 10
                digits += 1
            
            num = res
            print(num, digits)

            
        return num