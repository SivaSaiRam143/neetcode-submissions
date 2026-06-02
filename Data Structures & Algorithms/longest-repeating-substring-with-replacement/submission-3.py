class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_hash = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while left<=right and right < n:
            c_hash[s[right]]=c_hash.get(s[right],0)+1
            while not sum(c_hash.values())-max(c_hash.values())<=k:
                c_hash[s[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
            right+=1
        return ans


        