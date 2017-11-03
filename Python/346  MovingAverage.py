#346


# Time:  O(1)
# Space: O(w) w: the size


# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# For example,
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3


from collections import deque
class MovingAverage():
    def __init__(self,size):
        self.size=size
        self.data=deque()
        self.sum=0
    def next(self,val):
        if len(self.data)<size:
            self.data.append(val)
            return (sum(self.data)/len(self.data))
        else:
            self.data.popleft()
            self.data.append(val)
            return (sum(self.data)/size)
