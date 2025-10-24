class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        N = len(answerKey)
        l, r = 0, 0
        max_len1 = 0
        changes1 = 0
        for r in range(N):
            if answerKey[r] == 'F':
                changes1 += 1
            while changes1 > k:
                if answerKey[l] == 'F':
                    changes1 -= 1
                l += 1
            
            max_len1 = max(max_len1, r - l + 1)

        max_len2 = 0
        changes2 = 0
        l = 0
        for r in range(N):
            if answerKey[r] == 'T':
                changes2 += 1
            while changes2 > k:
                if answerKey[l] == 'T':
                    changes2 -= 1
                l += 1
            max_len2 = max(max_len2, r - l + 1)     
        return max(max_len1, max_len2)
        
        
        # N = len(answerKey)
        # l, r = 0, 0
        # # changes = {'T':'F', 'F':'T'}
        # maxf = 0
        # counts = defaultdict(int)
        # max_len = 0

        # for r in range(N):
        #     counts[answerKey[r]] += 1
        #     maxf = max(maxf, counts[answerKey[r]])

        #     while (r - l + 1) - maxf > k:
        #         counts[answerKey[l]] -= 1
        #         l += 1

        #     max_len = max(max_len, r - l + 1)

        # return max_len
