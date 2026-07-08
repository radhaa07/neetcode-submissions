class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = nums[0]
        for i in range(len(nums)):
            if i == 0 or i == 1:
                ans.append(nums[0])
                continue
            ans.append(left*nums[i-1])
            left *= nums[i-1]
        right = 1
        for i in range(len(ans)-1,-1,-1):
            if i == 0:
                ans[i] = right
                break
            ans[i] = right*ans[i]
            right*=nums[i]
        return ans