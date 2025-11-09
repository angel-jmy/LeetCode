class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
    
        def Once(first, last, st, points):
            stack = []
            tot_pnts = 0
            for i in range(len(st)):
                c = st[i]
                if not stack:
                    stack.append(c)
                else:
                    if c == last and stack[-1] == first:
                        stack.pop()
                        tot_pnts += points
                    else:
                        stack.append(c)

            return stack, tot_pnts

        if x > y:
            stack1, pnts1 = Once('a', 'b', s, x)
            t = ''.join(stack1)
            stack2, pnts2 = Once('b','a', t, y)
        else:
            stack1, pnts1 = Once('b', 'a', s, y)
            t = ''.join(stack1)
            stack2, pnts2 = Once('a','b', t, x)

            
        return pnts1 + pnts2