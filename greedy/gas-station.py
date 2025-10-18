class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0     # total gas - cost
        curr_tank = 0      # current segment's gas - cost
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            if curr_tank < 0:
                # Cannot reach station i+1 from start_index
                start_index = i + 1
                curr_tank = 0

        return start_index if total_tank >= 0 else -1
        
        
        
        
        
        # N = len(gas)

        # for i in range(N):
        #     curr_gas = 0
        #     for j in list(range(N))[i:] + list(range(N))[:i]:
        #         curr_gas += gas[j]
        #         curr_gas -= cost[j]
        #         if curr_gas < 0:
        #             break
        #     else: 
        #         return i

        # return -1

