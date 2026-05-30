class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_hash = {}
        for x in nums:
            c_hash[x] = c_hash.get(x,0) + 1

        # The max frequency any element can acheive is n
        # So we create an array of size n, where each element is a bucket[]
        # That bucket represents the frequency

        buckets = [[] for x in range(0,len(nums)+1)]

        for key,val in c_hash.items():
            buckets[val].append(key)
        
        ans = []
        for x in buckets[::-1]:
            for y in x:
                ans.append(y)
                if len(ans) == k:
                    return ans
        