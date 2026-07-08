class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_array(left,right):
            i,j=0,0
            result =[]
            n = len(left)
            m = len(right)
            while i < n and j < m:
                if left[i] <= right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            if i<n:
                while i< n:
                    result.append(left[i])
                    i+=1
            if j <m:
                while j<m:
                    result.append(right[j])
                    j+=1
            return result
        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            mid = (len(nums))//2
            left_half = nums[:mid]
            right_half = nums[mid:]
            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)
            return merge_array(left_half,right_half)
        return merge_sort(nums)

        