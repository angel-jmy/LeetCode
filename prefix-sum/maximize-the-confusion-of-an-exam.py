class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        N = len(answerKey)
        l, r = 0, 0
        # changes = {'T':'F', 'F':'T'}
        maxf = 0
        counts = defaultdict(int)
        max_len = 0

        for r in range(N):
            counts[answerKey[r]] += 1
            maxf = max(maxf, counts[answerKey[r]])

            while (r - l + 1) - maxf > k:
                counts[answerKey[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
            