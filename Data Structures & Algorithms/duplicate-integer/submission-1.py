class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # s = set()
        # for i in range(len(nums)):
        #     if nums[i] in s:
        #         return True
        #     s.add(nums[i])
        # return False
        hm ={}
        for i in nums:
           hm[i]= hm.get(i,0)+1
        for i in hm:
            if hm.get(i)>1:
                return True
        return False

        