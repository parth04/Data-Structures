
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

"""




class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """ 
        self.output = []
    def push(self, x: int) -> None:
        curr_min = self.getMin()
        if curr_min == None or curr_min > x:
            self.output.append((x,x))
        else:
            self.output.append((x,curr_min))
            

    def pop(self) -> None:
        if self.output:
            self.output.pop()
        else:
            return None

    def top(self) -> int:
        if self.output :
            return self.output[-1][0]
        else:
            return None
    def getMin(self) -> int:
        if self.output :
            return self.output[-1][1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
