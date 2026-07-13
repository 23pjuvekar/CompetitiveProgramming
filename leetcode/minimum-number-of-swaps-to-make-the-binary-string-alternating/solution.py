class Solution:
    def minSwaps(self, s: str) -> int:
        
        total = s.count("1")
        if abs(total - (len(s) - total)) > 1:
            return -1

        # zero first
        char = "0"
        zero_res_0 = 0
        zero_res_1 = 0
        for c in s:
            if char == "0":
                if char != c:
                    zero_res_0 += 1
                char = "1"
            else:
                if char != c:
                    zero_res_1 += 1
                char = "0"

        char = "1"
        one_res_0 = 0
        one_res_1 = 0
        for c in s:
            if char == "0":
                if char != c:
                    one_res_0 += 1
                char = "1"
            else:
                if char != c:
                    one_res_1 += 1
                char = "0"

        if zero_res_0 != zero_res_1:
            return one_res_0
        elif one_res_0 != one_res_1:
            return zero_res_0

        return (min(max(zero_res_0, zero_res_1), max(one_res_0, one_res_1)))
