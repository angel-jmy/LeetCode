class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N = len(s)

        def find_size(size):
            counts = defaultdict(int)
            window = defaultdict(int)
            uniques = 0
            for i in range(size):
                if s[i] not in window:
                    uniques += 1
                window[s[i]] += 1
            
            if uniques <= maxLetters:
                counts[s[:size]] += 1

            for r in range(size, N):
                l = r - size
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                    uniques -= 1
                if s[r] not in window:
                    uniques += 1
                window[s[r]] += 1
                if uniques <= maxLetters:
                    counts[s[l + 1:r + 1]] += 1
            
            if not counts:
                return 0
                
            return max(counts.items(), key = lambda x: x[1])[1]

        max_occur = 0

        for size in range(minSize, maxSize + 1):
            cur_number = find_size(size)
            max_occur = max(max_occur, cur_number)

        return max_occur