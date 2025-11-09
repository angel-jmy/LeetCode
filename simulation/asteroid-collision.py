class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        N = len(asteroids)
        last_left = False
        i = 0

        while i < N:
            if last_left:
                ast = last
            else:
                ast = asteroids[i]

            if res and res[-1] > 0 and ast < 0:
                if res[-1] + ast > 0:
                    i += 1
                    last_left = False
                elif res[-1] + ast < 0:
                    last = ast
                    last_left = True
                    res.pop()
                else:
                    res.pop()
                    i += 1
                    last_left = False
            else:
                res.append(ast)
                i += 1
                last_left = False


        return res