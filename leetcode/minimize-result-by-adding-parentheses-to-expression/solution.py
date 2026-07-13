class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split("+")

        best_value = float('inf')
        best_expr = ""
        for left in range(len(num1)):
            for right in range(1, len(num2) + 1):
                before = num1[:left]
                inside_left = num1[left:]
                inside_right = num2[:right]
                after = num2[right:]

                mult1 = int(before) if before else 1
                mult2 = int(after) if after else 1
                value = mult1 * (int(inside_left) + int(inside_right)) * mult2

                if value < best_value:
                    best_value = value
                    best_expr = f"{before}({inside_left}+{inside_right}){after}"
        return best_expr
