class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []

        for i in range(word_len):  # handle different start offsets
            left = i
            seen = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    seen[word] += 1
                    count += 1

                    # Too many of this word
                    while seen[word] > word_count[word]:
                        seen[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1

                    if count == num_words:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = j + word_len

        return res