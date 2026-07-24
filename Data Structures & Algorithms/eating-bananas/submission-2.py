class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) #rounds up for us
            if hours <= h:
                result = min(result, k) #since we want MINIMUM k
                right = k - 1 #want to try to find a smaller rate
            else:
                left = k + 1 #means rate was too small, need to find an even bigger rate
        return result


      