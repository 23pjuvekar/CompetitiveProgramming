class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        np, tp = 0, 0
        while np < len(name) and tp < len(typed):
            if name[np] == typed[tp]:
                np += 1
                tp += 1
            elif tp >= 1 and typed[tp] == typed[tp-1]:
                tp += 1
            else:
                return False

        if np != len(name):
            return False
        else:
            while tp < len(typed):
                if typed[tp] != typed[tp-1]:
                    return False
                tp += 1

        return True
