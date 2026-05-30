class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c_set = set()
        for x in nums:
            if x in c_set: return True
            c_set.add(x)
        return False
        