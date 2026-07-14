class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        prev = [1] * len(nums)
        suff = [1] * len(nums)

        # [1, 2, 4, 6] --> nums
        # [2, 4, 6, _]

        
        for n in range(1, len(nums)):
            prev[n] = nums[n-1] * prev[n-1] #prev = [1, 1, 2, 8] [48, 24, 6, 1]
        
        for n in range(len(nums) - 2, -1, -1):
            suff[n] = nums[n+1] * suff[n+1] #[1, 1, 1, 1]
        
        for i in range(len(nums)):
            nums[i] = prev[i] * suff[i]

        return nums