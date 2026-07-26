class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            for j in range(i+1,n):
                if nums[j] == nums[j-1] and j > i+1:
                    continue
                left = j+1
                right = len(nums)-1
                while left<right:
                    ans = nums[i]+nums[j]+nums[left]+nums[right]
                    if ans == target:
                        temp =[nums[i],nums[j],nums[left],nums[right]]
                        result.add(tuple(temp))
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  
                        left+=1
                        right-=1
                    elif ans < target:
                        left+=1
                    else:
                        right-=1
        final = []
        for i in result:
            final.append(list(i))

        return final
        
        
        