class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        ans = -1
        for i in range(1, len(prices)):
            if prices[i] > min_val:
                if ans < (prices[i]-min_val):
                    ans = prices[i]-min_val
            else:
                min_val = prices[i]
        return ans if ans !=-1 else 0       