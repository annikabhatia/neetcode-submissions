class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # BRUTE FORCE WAY
        # have a for loop that goes through each element
        # set left to that element, and have right iterate until you find a value that is larger than the left
        # find the difference between (index of right) - (index of left), and assign that to count
        # replace the element with the count

        # MONOTONIC DECREASING STACK    
        
        res = [0] * len(temperatures)
        stack = [] # pair: [temp,index]

        for i, t in enumerate(temperatures):
            #while the stack is not empty and the temperature is greater than the previous element
            while stack and t > stack[-1][0]:
                #LIFO for stack, so pop the top element
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res

        