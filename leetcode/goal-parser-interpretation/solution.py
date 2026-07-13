class Solution:
    def interpret(self, command: str) -> str:

        res = ""
        for i in range(len(command) - 1):
            if command[i] == "(" and command[i + 1] == ")":
                res += "o"
            if command[i] != "(" and command[i] != ")":
                res += command[i]
        if command[-1] != "(" and command[-1] != ")":
                res += command[-1]
        return res
