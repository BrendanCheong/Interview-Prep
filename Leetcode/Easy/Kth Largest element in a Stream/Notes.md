# Kth Largest Element in A Stream

Using a binary heap we can solve this problem

given [4, 5, 2, 5], k = 2
lets sort the list first, when converting a list into a binary MIN heap in O(N) time.
so its: [2, 4, 5, 5], with the kth largest element being 5.
NOTE: Min heap does not auto sort the whole list when a new element is added.

# The Trick
The trick here is that in order to find the **Kth largest element**, we must **discard** a certain amount of elements until we reach **size of heap == kth**
which is O((N - k) log k) time!

[2, 5, 4, 5] remove 2 elements
[4, 5, 5]
[5, 5]

# Brute Force + Other Approaches
1. Brute force would be to add and sort, this takes O(n log n) for each operation, at least indexing is O(1) time
2. Another approach would be to **binary search** O(log n) time after sorting once, to find **the right place to insert** the new number. However **inserting takes O(n) time since we need to reshuffle the indexes of the array**.