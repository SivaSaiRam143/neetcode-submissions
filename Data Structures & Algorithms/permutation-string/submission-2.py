class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):return False
        l_hash = {}
        for x in s1:
            l_hash[x] = l_hash.get(x,0)+1
        left = 0
        right = len(s1)-1
        r_hash = {}
        for i in range(right+1):
            if s2[i] in l_hash:
                r_hash[s2[i]] = r_hash.get(s2[i], 0) + 1
        n = len(s2)
        while right < n:
            if l_hash == r_hash:
                return True
            if s2[left] in l_hash : r_hash[s2[left]]-=1
            left+=1
            right+=1
            if right < n and s2[right] in l_hash: r_hash[s2[right]] = r_hash.get(s2[right],0)+1
        return False


        