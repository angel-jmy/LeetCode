class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        l, r = 0, 0
        max_len = 0
        seq = deque()              # window buffer
        counts = defaultdict(int)  # char -> count in window
        maxf = 0                   # most frequent char count in window

        while r < N:
            ch = s[r]
            seq.append(ch)
            counts[ch] += 1
            if counts[ch] > maxf:
                maxf = counts[ch]

            # shrink while we need more than k replacements
            while len(seq) - maxf > k:
                left = seq.popleft()
                counts[left] -= 1
                l += 1

            # update best length
            if r - l + 1 > max_len:
                max_len = r - l + 1

            r += 1

        return max_len