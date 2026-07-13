class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        arr = s.split(" ")
        nums = []

        for a in arr:
            if a.isdigit():
                if nums and nums[-1] >= int(a):
                    return False
                nums.append(int(a))
        return True
