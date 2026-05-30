class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c_hash = {}
        for i in range(len(nums)):
            if target-nums[i] in c_hash: return [c_hash[target-nums[i]], i]
            c_hash[nums[i]] = i
        
        