class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t): return False
        c_hash = {}
        for x in s:
            c_hash[x] = c_hash.get(x,0) + 1
        for y in t:
            if y in c_hash:
                c_hash[y]-=1
                if c_hash[y]<0: return False
            else:
                return False
        return True