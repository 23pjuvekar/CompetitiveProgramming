class Solution:
    def smallestNumber(self, num: int) -> int:

        if num < 0:
            num = list(str(num)[1:])
            num.sort(reverse=True)
            return int("-" + "".join(num))
        else:
            num = list(str(num))
            num.sort()
            for i in range(len(num)):
                if num[i] != "0":
                    val = num[i]
                    num.remove(val)
                    num.insert(0, val)
                    break
            print(num)
            return int("".join(num))
