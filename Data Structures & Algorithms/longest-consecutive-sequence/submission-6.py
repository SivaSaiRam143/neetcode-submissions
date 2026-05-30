class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:return 0
        max_ele = max(nums)+1
        min_ele = min(nums)
        min_seen = []
        if min_ele < 0:
            min_seen = [0]*(-1*min_ele+1)
            for x in nums:
                if x<0:
                    min_seen[x*-1] = 1
            min_seen = min_seen[::-1]
        
        min_seen = min_seen[0:len(min_seen)-1]

        seen = [0]*max_ele
        for x in nums:
            if x>=0:
                seen[x] = 1
        seen = min_seen + seen
        ans = 0
        counted = 0
        for i in range(len(seen)):
            if seen[i] == 0:
                ans = max(ans, counted)
                counted = 0
            else:
                counted+=1
        return max(ans, counted)
