class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        ans = right
        while left<=right:
            mid = left+ (right-left) // 2
            cal_hours = 0
            for pile in piles:
                if pile <= mid:
                    cal_hours += 1
                else:
                    cal_hours += (pile // mid) + (1 if pile%mid >0 else 0)
            if cal_hours > h:
                left = mid+1
            else:
                if ans < mid:
                    return ans
                else:
                    ans = mid
                right = mid-1
        return ans
