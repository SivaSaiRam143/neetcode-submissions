class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_hash = {}
        for x in s:
            if x in c_hash: 
                c_hash[x]+=1
            else:
                c_hash[x]=1
        for y in t:
            if y in c_hash:
                c_hash[y]-=1
                if c_hash[y]<0: return False
            else:
                return False

        if sum(c_hash.values())>=1:
            return False
        return True