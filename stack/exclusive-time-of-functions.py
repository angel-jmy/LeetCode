class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n

        running = [] # stores the index, and start time, as a tuple, maximum capacity = 1
        paused = [] # index
        for log in logs:
            idx, action, ts = log.split(":")
            idx, ts = int(idx), int(ts)
            if action == 'start':
                if running:
                    i, t = running.pop()
                    paused.append(i)
                    res[i] += ts - t
                
                running.append((idx, ts))
            
            elif action == 'end':
                _, t = running.pop()
                res[idx] += ts - t + 1
                if paused:
                    i = paused.pop()
                    running.append((i, ts + 1))

        return res
