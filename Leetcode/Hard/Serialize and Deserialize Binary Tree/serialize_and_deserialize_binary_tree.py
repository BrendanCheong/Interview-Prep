# link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        PreorderTraversal is:
        root -> left -> right
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node: TreeNode) -> None:
            if not node:
                # if not node usually we return None to show no subtree.
                # in this case we must append 'null' to show that there is no subtree.
                res.append('null')
                return None
            # start off from the root node first, this is preorder traversal
            # root -> left -> right
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            # we are guaranteed to have null, aka the tree will end, so no need for a return statement
        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_array = data.split(',')
        self.POINTER: int = 0 # start from first index

        def dfs(arr: List[str]) -> TreeNode:
            # here we plan to start from the start of the array, then move left to right
            # our pointer will move from the start of the array to the end
            # base case is if the array is null, then tree has ended
            # edge case: the tree has only null nodes, so no tree.
            if arr[self.POINTER] == 'null':
                self.POINTER += 1
                return None
            # root -> left -> right
            root = TreeNode(int(arr[self.POINTER]))
            self.POINTER += 1
            root.left = dfs(arr)
            root.right = dfs(arr)
            return root
        return dfs(tree_array)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))