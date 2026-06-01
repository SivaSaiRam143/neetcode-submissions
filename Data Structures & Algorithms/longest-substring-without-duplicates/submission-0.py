class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [0]*256
        left, right = 0,0
        ans = 0
        n = len(s)
        while left<=right and right < n:
            while seen[ord(s[right])] == 1 and left<=right:
                seen[ord(s[left])] = 0
                left+=1
            seen[ord(s[right])] = 1
            right +=1
            ans = max(ans, right-left)
        return ans
        