class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_st = ""
        for x in s:
            if x.isalnum():
                refined_st += x.lower()
        a = 0
        b = len(refined_st)-1
        while a <= b:
            if refined_st[a] != refined_st[b]:
                return False
            a+=1
            b-=1
        return True
        