class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        answer = set()

        #[-4, -1, -1, 0, 1, 2]
        
        #so there is at least 2 indices after for 1)left and 2)right to occupy
        for n in range(len(nums) - 2):
            #smallest value to consider
            left = n+1
            #largest value left to consider
            right = len(nums)-1

            #so left and right never point to same index
            while left < right:
                if nums[left] + nums[n] + nums[right] < 0:
                    left+=1
                elif nums[left] + nums[n] + nums[right] > 0:
                    right-=1
                else:
                    answer.add((nums[left], nums[n], nums[right]))
                    left+=1
                    right-=1
            
        return [list(t) for t in answer]

            
            




        