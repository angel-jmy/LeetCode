class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = 0
        l = 0
        min_stack, max_stack = deque(), deque()
        for r, x in enumerate(nums):
            while max_stack and x > nums[max_stack[-1]]:
                max_stack.pop()
            max_stack.append(r)
            while min_stack and x < nums[min_stack[-1]]:
                min_stack.pop()
            min_stack.append(r)
            while max_stack and min_stack and (nums[max_stack[0]] - nums[min_stack[0]]) > 2:     
                if max_stack[0] <= l:
                    max_stack.popleft()
                if min_stack[0] <= l:
                    min_stack.popleft()            
                l += 1 

            counts += r - l + 1
        return counts