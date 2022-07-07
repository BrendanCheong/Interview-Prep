# Sort Colors

The solution is to do something similar to the Dutch National Flag Quicksort partition algorithm

given that we want 0, 1, 2 in this particular order
we can keep track of 3 pointers, where we **always want** the **'0' at the leftmost side of the array** and the **'2' at the rightmost side** of the array.
And we want the **'1' at the middle**

So when we do a single O(n) iteration through the array, we want to swap **the '1' with the '0', or push all the colors to their respective places** and **'1' with '2' we must push them to the right**

- so we if we encounter a 0, we will swap it with the leftmost pointer, move the leftmost pointer after its finished swapping as the number is already in place. **Move pointer towards the right** and move **'1' pointer to the right was well** or else the next iteration won't do anything.
- encounter a 2, swap it with rightmost pointer, move the rightmost pointer after its finished swapping, as the number is already in place. **Move pointer towards the right**. Don't increase '1' pointer as **the swapped number might be either a '0' or a '1'** in which case it needs to be swapped again if '0'.
- if encounter a 1, move on to the next number as its already in place.

1, 2, 0, 1
</br>
1, 1, 0, 2
</br>
0, 1, 1, 2
</br>
done

**You can terminate early** if the '1' pointer exceeds the '2' pointer
# Brute Force + Other solutions
