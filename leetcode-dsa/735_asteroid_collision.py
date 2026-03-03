class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        res = []

        for i in range(len(asteroids)):
            while res and res[-1] > 0 and asteroids[i] < 0:
                sum = res[-1] + asteroids[i]
                if sum > 0:
                    break
                elif sum < 0:
                    res.pop()
                    continue
                else:
                    res.pop()
                    break
            else:
                res.append(asteroids[i])
        
        return res