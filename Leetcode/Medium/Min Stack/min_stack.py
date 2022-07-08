#link: https://leetcode.com/problems/min-stack/submissions/

TOP = -1

class MinStack:
    """
    Time Complexity: O(1) operations
    Space Complexity: O(N), no way to save on space for the self.min_stack unfortunately
    """

    def __init__(self):
        self.norm_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.norm_stack.append(val)
        if (not len(self.min_stack)):
            # edge case here we must add to the min stack if its empty, as there will always be a solution
            self.min_stack.append(val)
            return
            # NOTE: Remember to exit after completing the edge case

        min_stack_top = self.min_stack[TOP]
        if (val <= min_stack_top):
            # NOTE: remember that less than or EQUALS is important
            # or else there WILL BE AN OUT OF BOUNDS ERROR
            self.min_stack.append(val)

    def pop(self) -> None:
        # only pop from the min stack for the edge case where the top of the norm stack
        # so happens to be the same as the top of the min stack
        if (self.min_stack[TOP] == self.norm_stack[TOP]):
            self.min_stack.pop()
        
        self.norm_stack.pop()

    def top(self) -> int:
        return self.norm_stack[TOP]
        
    def getMin(self) -> int:
        return self.min_stack[TOP]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()