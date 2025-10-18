class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        
        num = 0
        sign = 1
        
        for i, ch in enumerate(s):
            if i == 0 and ch == '-':
                sign *= -1
                continue
                
            if i == 0 and ch == '+':
                continue
                
            if not ch.isnumeric():
                break
            
            
            num = num * 10 + int(ch)
           
        
        num = num * sign
        
        if num < -2**31:
            return -2 ** 31
        if num > 2**31 - 1:
            return 2**31 - 1
        
        return num
            
            
        
        
        
        