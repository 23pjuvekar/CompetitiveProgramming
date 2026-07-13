class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:


        num_e = []
        num_o = []
        target_e = []
        target_o = []


        for n in nums:
            if n % 2 == 0:
                num_e.append(n)
            else:
                num_o.append(n)
        
        for n in target:
            if n % 2 == 0:
                target_e.append(n)
            else:
                target_o.append(n)
        
        num_e.sort()
        num_o.sort()
        target_e.sort()
        target_o.sort()

        up_change = 0
        down_change = 0

        for i in range(len(target_e)):
            if target_e[i] > num_e[i]:
                up_change += ((target_e[i] - num_e[i]) // 2)
            else:
                down_change += ((num_e[i] - target_e[i]) // 2)

        for i in range(len(target_o)):
            if target_o[i] > num_o[i]:
                up_change += ((target_o[i] - num_o[i]) // 2)
            else:
                down_change += ((num_o[i] - target_o[i]) // 2)

        return up_change
