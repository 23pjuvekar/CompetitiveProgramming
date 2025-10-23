class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""
        stack = []

        for item in path.split("/"):
            if item == "..":
                if stack:
                    stack.pop()
            elif item != "." and item != "":
                stack.append(item)
        
        for item in stack:
            res += ("/" + item)
        if res == "":
            return "/"
        return res
        