class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)

    def binary_search(self, nums, left, right, target):
        print(nums, left, right, target)
        ans = -1
        if left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid] and nums[left] <= target <= nums[mid]:
                return self.binary_search(nums, left, mid-1, target)
            elif nums[right] >= nums[mid] and nums[mid] <= target <= nums[right]:
                return self.binary_search(nums, mid+1, right, target)
            elif nums[left] <= nums[mid]:
                return self.binary_search(nums, mid+1, right, target)
            else:
                return self.binary_search(nums, left, mid-1, target)
        
        return ans


        