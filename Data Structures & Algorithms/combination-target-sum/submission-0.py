class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def dfs(i, su):
            if su == target:
                result.append(curr.copy())
                return

            if i == len(nums) or su > target:
                return        
            
            curr.append(nums[i])
            dfs(i, su + nums[i])
            
            curr.pop()
            dfs(i+1, su)
        
        dfs(0,0)
        return result