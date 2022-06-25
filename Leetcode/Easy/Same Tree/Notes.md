# Same Tree

## Recursion
Here we have to think about recursion. We must first find the
1. Terminating base case
2. The return case when we find the value

In this case, when we traverse each tree, we can encounter `null` values. So when that happens, one of the nodes for either Tree1 or Tree2
is null. So to see if there are the same tree, the other node must also be null as well

Otherwise, each **node value must equal the other node value**. Note that `p.val` when `p = None` is a TypeError, which is why we have the base case.

To traverse each tree at the same time, we do `self.isSameTree(p.left, q.left)` where it must also equal `self.isSameTree(p.right, q.right)`
