from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.count = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.count.append(t)

        while self.count and t - self.count[0] > 3000:
            self.count.popleft()
        
        return len(self.count)