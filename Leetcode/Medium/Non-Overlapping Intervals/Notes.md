# Non-overlapping Intervals

First we sort them in O(n log n), don't look at them in a random order

1. The minimum number of removals is when we **remove the interval with the LARGEST end time**
2. So we must **leave the SMALLEST end time** alone, and just remove what we need to remove


```
        --------
    --------  -------
here we remove the top interval, if we removed the bottom left interval instead, the top interval may still overlap with the right interval    
```
# Brute Force
Check every possibility, in O(2^n)