class Solution:
    def findMin(self, nums: List[int]) -> int:
    #the neetcode solution, maybe more efficient?
        res = nums[0]
        left = 0 
        right = len(nums) - 1

        while left <= right:
            #case for when array is same as orig array (rotated n times)
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            m = (left+right) // 2
            res = min(res, nums[m])
            #search right
            if nums[m] >= nums[left]:
                left = m+1
            #search left
            else:
                right = m - 1
        return res
        