class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        m = float('inf')
        left = 0

        for right in range(len(nums)):

            s += nums[right]

            while s >= target:

                m = min(m, right - left + 1)

                s -= nums[left]
                left += 1
        if m == float('inf'):
            return 0
        return m
                