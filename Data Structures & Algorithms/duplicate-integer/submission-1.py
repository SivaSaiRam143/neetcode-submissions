class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c_hash = {}
        for x in nums:
            if x in c_hash: return True
            c_hash[x] = 1
        return False
        