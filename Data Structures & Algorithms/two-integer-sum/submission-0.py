class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in hm:
                return [hm.get(ans), i]
            hm[nums[i]] = i
        