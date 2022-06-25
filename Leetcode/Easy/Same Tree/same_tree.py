#link: https://leetcode.com/problems/same-tree/submissions/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Solution is in O(N) time, where we go through the root first, then the left tree then the right tree
        similar to DFS or Pre-order traversal.
        Although you could go right then left then root, or any other kind of traversal
        You could also turn your tree into an array or string by serializing it,
        then doing TreeArr1 == TreeArr2.
        However, it takes less O(N) loops to just traverse both at the same time
        """
        # base case, p.val == q.val, we must check the value
        # base case, eventually one of the values will be None, where there are no subtrees, at this stage
        # check to see if the current None node for one of the Tree is also None for the other Tree at its current node!
        # to traverse, we can go to the left subtree for both trees
        # and can then go to the right subtree after that
        if not p or not q:
            return p == None and q == None
        return p.val == q.val and (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        