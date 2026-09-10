class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        s = 0
        m = float('inf')
        left = 0

        for right in range(len(nums)):

            s += nums[right]

            while s >= target:

                m = min(m, right - left + 1)

                s -= nums[left]
                left += 1
        return m
                