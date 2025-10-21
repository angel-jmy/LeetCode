class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        counts = Counter(blocks[:k])
        min_ops = counts['W']
        curr_ops = min_ops
        if min_ops == 0:
            return 0

        for i in range(k, N):
            left = i - k
            if blocks[left] == 'W' and blocks[i] == 'B':
                curr_ops -= 1
            elif blocks[left] == 'B' and blocks[i] == 'W':
                curr_ops += 1

            min_ops = min(min_ops, curr_ops)

        return min_ops