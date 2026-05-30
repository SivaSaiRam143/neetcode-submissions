class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_hash = {}
        for x in nums:
            c_hash[x] = c_hash.get(x,0)+1
        sorted_eles = sorted(c_hash.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_eles[:k]]
        