class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        length = 0
        central = False

        for word in count:
            rev = word[::-1]
            if word == rev:
                # Use pairs like "gg" + "gg"
                pairs = count[word] // 2
                length += pairs * 4
                if count[word] % 2 == 1:
                    central = True  # One leftover can be in the middle
            else:
                if rev in count:
                    # Pair word with its reverse
                    pair_count = min(count[word], count[rev])
                    length += pair_count * 4
                    # Avoid double-counting
                    count[rev] = 0

        if central:
            length += 2  # One central palindromic word

        return length
            