class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)  # intersection: min count for each character

        result = []
        for char, count in common.items():
            result.extend([char] * count)

        return result