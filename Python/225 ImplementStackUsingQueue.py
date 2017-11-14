#225


# Time:  push: O(n), pop,top,empty: O(1)
# Space: O(n)


# Implement the following operations of a stack using queues.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- 
# which means only push to back, peek/pop from front, size,
# and is empty operations are valid.
# Depending on your language, queue may not be supported natively. 
# You may simulate a queue by using a list or deque (double-ended queue), 
# as long as you use only standard operations of a queue.
# You may assume that all operations are valid
# (for example, no pop or top operations will be called on an empty stack).




import collections
class queue():
    def __init__(self):
        self.data=collections.deque()
    def push(self,val):
        self.data.append(val)
    def pop(self):
        self.data.popleft()
    def peek(self):
        return self.data[0]
    def size(self):
        return len(self.data)
    def isempty(self):
        return len(self.data)==0
    
class stack():
    def __init__(self):
        self.data=queue()
    def push(self,val):
        self.data.push(val)
        for _ in range(self.data.size()-1):
            self.data.push(self.data.peek())
            self.data.pop()
    def pop(self):
        self.data.pop()
    def top(self):
        return self.data.peek()
    def empty(self):
        return self.data.isempty()
