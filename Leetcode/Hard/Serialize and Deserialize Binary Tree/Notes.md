# Serialize and Deserialize a Binary Tree

There are many approaches:
- DFS (preorder traversal)
- BFS (levelorder traversal)
- Sorting tree (inorder traversal)

# Edge cases
- We can assume if empty tree, it will be an array of null like [null]
- tree will always have null to indicate that there are no more subtrees

## DFS version
Given the binary tree as follows: root = [1,2,3,null,null,4,5]
we have the tree as such
            1
        2       3
      n   n    4  5
we can use **DFS** to have a **pre-order traversal** to serialize the tree, by traversing starting from the root.

root -> left -> right

we assume that the binary tree can be **complete or incomplete**.

DFS means we start from the root, then we **visit the left subtree until completion** followed by visiting the **right subtree until completion**. 
We will have to backtrack to find the right subtree.
If we hit a null, it means that **we cannot go any further and we must backtrack or unfold the recursion stack**

### Serialize
we will have an array. Then as we traverse the tree using DFS, add to the array. Using python we can turn that array into a string using `','.join(arr)`

### Deserialize
we are given a string and must turn it into a tree. This one is a bit tricky.

first we can make the string into an array so its easier to traverse. This one takes O(N) time.
The rest of the pre-order traversal takes O(N) time, so O(N) total
we can recursively go through the array via DFS, by first going through all the left subtrees and using a pointer to figure out which is the next index to go to, where the pointer starts from the first index and goes all the way to the end of the array.

it only stops when we hit a null value, we there are no more subtrees, causing the recursion to unwind and backtrack to find the right subtree.

similarly you can implement this using a queue as well.