class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        #binary search needs to repeat while low <= high
        while low <= high:
            mid = (low+high) // 2
            if target > nums[mid]:
                #need the +1 to shrink the range
                low = mid + 1
            elif target < nums[mid]:
                #need the -1 to shrink the range
                high = mid - 1
            elif target == nums[mid]:
                return mid
        return -1