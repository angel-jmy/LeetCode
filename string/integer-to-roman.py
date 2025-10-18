class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapping = {0:'', 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

        level = 1
        res = ""

        while num > 0:
            tail = num % 10
            
            if tail != 4 and tail != 9:
                res = mapping[tail // 5 * 5 * level] + mapping[level] * (tail % 5) + res
            
            else:
                res = mapping[level] + mapping[(tail + 1) * level] + res
                
            num = num // 10
            level *= 10

        return res