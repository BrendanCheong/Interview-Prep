class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Seems like a 2 pointer problem, with O(n) traversal and O(1) space
        
        keep a pointer on s, and a pointer on t. Keep iterating from t to its end to find the first letter on s. If found, move s pointer forward. Continue doing so until s pointer is at len(s)
        
        2 pointers is the simpliest most straight forward solution with smallest space cost. Granted, its not
        very extenable if the problem changes to have n number of string s to find...
        """
        pointer_s, end_pointer_s = 0, len(s)
        # specific edge case where empty strings are always a substring of t
        if not s:
            return True
        
        # keep moving the pointer of s until it reaches the end of s
        # if we never reached the end, its false
        for i, ele in enumerate(t):
            target = s[pointer_s]
            if (ele == target):
                pointer_s += 1
            if (pointer_s == end_pointer_s):
                return True
        return False

# test cases
sol = Solution()
assert sol.isSubsequence("abc", "ahbgdc") == True
assert sol.isSubsequence("axc", "ahbgdc") == False
assert sol.isSubsequence("acb", "ahbgdc") == False
assert sol.isSubsequence("abc", "abc") == True
assert sol.isSubsequence("abc", "ab") == False
assert sol.isSubsequence("", "abcc") == True