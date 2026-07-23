class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #list comprehension, we can also use a hashmap
        #zip() walks through both lists in parallel and pairs up elements that share the same index.
        pair = [[p, s] for p,s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            
