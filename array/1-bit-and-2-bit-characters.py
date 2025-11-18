class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        N = len(bits)
        i = 0
        while i < N:
            if i == N - 1 and bits[i] == 0:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return False
