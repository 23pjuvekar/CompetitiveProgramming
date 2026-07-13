class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for item in items:
            if (ruleKey == "type" and ruleValue == item[0]) or (ruleKey == "color" and ruleValue == item[1]) or (ruleKey == "name" and ruleValue == item[2]):
                res += 1
        return res
