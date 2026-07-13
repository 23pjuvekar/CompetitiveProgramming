class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            current_height = heights[i]
            seen_count = 0

            while stack and heights[stack[-1]] <= current_height:
                stack.pop()
                seen_count += 1

            if stack:
                seen_count += 1

            ans[i] = seen_count
            stack.append(i)

        return ans
