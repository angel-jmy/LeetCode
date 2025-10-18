class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        maps = {c:v for c, v in zip(chars, vals)}
        counts = Counter(s)
        new_map = {}
        for c in counts.keys():
            if c in maps.keys():
                new_map[c] = maps[c]
            else:
                new_map[c] = ord(c) - ord('a') + 1

        prefs = [0]
        for c in s:
            prefs.append(new_map[c] + prefs[-1])


        min_sum = 0
        max_sum = 0
        for p in prefs[1:]:
            
            max_sum = max(max_sum, p - min_sum)
            min_sum = min(min_sum, p)
        
        return max_sum