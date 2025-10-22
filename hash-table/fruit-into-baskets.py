class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        l, r = 0, 0
        max_len = 0

        counts = defaultdict(int)
        types = 0

        for r in range(N):
            if fruits[r] not in counts and types <= 1:
                counts[fruits[r]] += 1
                types += 1
            elif fruits[r] in counts:
                counts[fruits[r]] += 1
            else:
                while fruits[r] not in counts and types >= 2:
                    counts[fruits[l]] -= 1
                    if counts[fruits[l]] == 0:
                        del counts[fruits[l]]
                        types -= 1

                    l += 1

                counts[fruits[r]] += 1
                types += 1

            max_len = max(max_len, r - l + 1)


        return max_len