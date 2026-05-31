class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums = sorted(nums)
        print(nums)
        for i, num in enumerate(nums):
            a = i+1
            b = n-1
            while a<b:
                if num + nums[a] + nums[b] == 0:
                    if (num,nums[a],nums[b]) not in ans : ans.append((num,nums[a],nums[b]))
                    a+=1
                elif num +nums[a] + nums[b] > 0:
                    b-=1
                else:
                    a+=1
        return ans       