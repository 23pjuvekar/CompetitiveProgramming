class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = []
        stack = []
        
        for index in range(len(position)):
            pairs.append([position[index], speed[index]])
        
        pairs.sort(reverse=True)

        for pair in pairs:
            stack.append((target - pair[0]) / pair[1])
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)
