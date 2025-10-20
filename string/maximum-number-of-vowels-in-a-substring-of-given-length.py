class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        N = len(s)
        max_len, curr_len = 0, 0

        for c in s[:k]:
            if c in vowels:
                curr_len += 1
                
        max_len = max(max_len, curr_len)

        for i in range(k, N):
            left = i - k
            if s[left] in vowels:
                curr_len -= 1
            if s[i] in vowels:
                curr_len += 1
            
            max_len = max(max_len, curr_len)

        return max_len