class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid_indices = set()
        stack = []
        
        # Identify invalid parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    invalid_indices.add(i)
                else:
                    stack.pop()
        
        # Add unmatched '(' indices to invalid set
        invalid_indices.update(stack)
        
        # Build the result string
        res = [char for i, char in enumerate(s) if i not in invalid_indices]
        
        return ''.join(res)
