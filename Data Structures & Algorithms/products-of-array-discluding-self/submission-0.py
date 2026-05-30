class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        if len(nums) == 1: return nums
        forward_product = [1]*len(nums)
        backward_product = [1]*len(nums)
        forward_product[0] = nums[0]
        backward_product[-1] = nums[-1]
        for i in range(1, len(nums)):
            forward_product[i] = forward_product[i-1]*nums[i]
            backward_product[len(nums)-1-i] = backward_product[len(nums)-i]*nums[len(nums)-1-i]
        ans = [0]*len(nums)
        ans[0] = backward_product[1]
        ans[-1] = forward_product[len(nums)-2]
        for i in range(1, len(forward_product)-1):
            ans[i] = (forward_product[i-1]*backward_product[i+1])
        return ans