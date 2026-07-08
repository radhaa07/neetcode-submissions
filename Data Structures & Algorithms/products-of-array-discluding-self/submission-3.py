class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            ans[i] = left
            left*=nums[i]
        right = 1
        for i in range(len(ans)-1,-1,-1):
            ans[i] = right*ans[i]
            right*=nums[i]
        return ans