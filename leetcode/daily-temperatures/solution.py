# Use a stack of pairs

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        res = [0] * len(temperatures)
        min_stack = []

        for index, temp in enumerate(temperatures):
            while min_stack and min_stack[-1][0] < temp:
                temp_pop, index_pop = min_stack.pop()
                res[index_pop] = index - index_pop
            min_stack.append((temp, index))
        
        return res
