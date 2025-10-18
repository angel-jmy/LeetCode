class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        length = len(ransomNote)

        while length > 0:
            c = ransomNote[0]

            if c not in magazine:
                return False
            else:
                ransomNote = ransomNote[1:]
                magazine = magazine[:magazine.find(c)] + magazine[magazine.find(c) + 1:]        

                length -= 1        
        
        return True