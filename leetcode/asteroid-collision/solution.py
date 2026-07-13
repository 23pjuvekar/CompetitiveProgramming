class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for a in asteroids:
            stack.append(a)
            while len(stack) > 1:
                if stack[-2] > 0 and stack[-1] < 0:
                    if abs(stack[-1]) == abs(stack[-2]):
                        latest = stack.pop()
                        second_lastest = stack.pop()
                        continue
                    else:
                        latest = stack.pop()
                        second_lastest = stack.pop()
                        if abs(latest) > abs(second_lastest):
                            stack.append(latest)
                        else:
                            stack.append(second_lastest)
                else:
                    break
        return stack
