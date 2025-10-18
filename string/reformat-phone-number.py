class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number = number.replace(' ', '').replace('-', '')

        res = []
        i = 0
        N = len(number)

        while N - i > 4:
            res.append(number[i:i+3])
            i += 3

        # Handle remaining digits
        if N - i == 4:
            res.append(number[i:i+2])
            res.append(number[i+2:])
        else:
            res.append(number[i:])

        return '-'.join(res)