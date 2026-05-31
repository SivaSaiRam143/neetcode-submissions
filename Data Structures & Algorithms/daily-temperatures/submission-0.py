class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = [(temperatures[0], 0)]
        temp_len = len(temperatures)
        ans = [0]*temp_len
        for i in range(1, len(temperatures)):
            while len(my_stack) > 0 and my_stack[-1][0] < temperatures[i]:
                ans[my_stack[-1][1]] = i-my_stack[-1][1]
                my_stack.pop()
            my_stack.append((temperatures[i], i))
        return ans        