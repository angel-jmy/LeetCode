class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        N = len(s)
        if k == N:
            return 1
            
        xsum = ysum = 0

        points = set()
        counter = 0
        
        for i in range(k):
            xsum += 1 if s[i] == 'R' else -1 if s[i] == 'L' else 0
            ysum += 1 if s[i] == 'U' else -1 if s[i] == 'D' else 0

        for i in range(k, N):
            xsum += 1 if s[i] == 'R' else -1 if s[i] == 'L' else 0
            ysum += 1 if s[i] == 'U' else -1 if s[i] == 'D' else 0

            left = i - k
            xsum -= 1 if s[left] == 'R' else -1 if s[left] == 'L' else 0
            ysum -= 1 if s[left] == 'U' else -1 if s[left] == 'D' else 0

            if (xsum, ysum) in points:
                continue
            else:
                counter += 1
                points.add((xsum, ysum))

        return counter
            

