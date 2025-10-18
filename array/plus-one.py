class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        N = len(digits)
        
        number = 0
        
        for i in range(N):
            number += 10**i * digits[N - i - 1]
            
        number += 1
        
        digits1 = []
             
        while number > 0 and number // 10 >= 0:
            digits1.insert(0, number % 10)
            number //= 10
         
        return digits1
        
        