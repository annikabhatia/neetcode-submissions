class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                #still want to add that index but then stop the process since we found our two integers
                return [seen[diff], index] 
            else:
                seen[num] = index
        