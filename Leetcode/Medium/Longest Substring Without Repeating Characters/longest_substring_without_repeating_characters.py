# link: https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute force solution would be to generate all possible substrings
        in O(n^2) time and storing them in a dict, with the <k:v> being <substring: len(substring)>. Then I would try to find the longest substring
        by making sure that the length of the substring created is equal to the len(set(substring)) as this would mean that there are no repeating
        characters in the substring. Then use the max function to find the longest substring. 
        """
        # ans = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         sub = s[i:j+1]
        #         if len(set(sub)) == len(sub):
        #             ans = max(ans, len(sub))
        # return ans
        """
        We can assume there are multiple unique solutions to this qns
        The more optimal solution would be to use a sliding window.
        First check to see if empty string, if it is then return 0.
        we will first create an empty set(), then we start with 2 pointers. In the beginning each pointer is on the first index
        of the string. 
        1. since we start from 0, check if the right pointer is not in the set, if its not, then we add it into the set.
        2. next we must move the right pointer to the right and then we will find the ans = max(ans, len(set)).
        3. if instead we encounter a duplicate, just increment the left pointer, AND remove the element of the left pointer from the set,
        as we have found a duplicate, where s[left] == s[right] so we just need one unique character.
        4. this is a sliding window algo, we must keep going forwards until we find that right > len(s) or out of bounds, then return ans as we have reached
        the end

        This is a O(n) solution, with each operation in the set/hashtable being O(1) time. (amortized to be exact)
        """
        ans = 0
        if len(s) == 0:
            return ans
        _set = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in _set:
                _set.add(s[right])
                right += 1
                ans = max(ans, len(_set))
            else:
                left += 1
                _set.remove(s[left])
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
print(sol.lengthOfLongestSubstring("bbbbb"))
assert sol.lengthOfLongestSubstring("bbbbb") == 1
print(sol.lengthOfLongestSubstring("pwwkew"))
assert sol.lengthOfLongestSubstring("pwwkew") == 3
print(sol.lengthOfLongestSubstring(""))
assert sol.lengthOfLongestSubstring("") == 0
print(sol.lengthOfLongestSubstring(" "))
assert sol.lengthOfLongestSubstring(" ") == 1
print(sol.lengthOfLongestSubstring("au"))
assert sol.lengthOfLongestSubstring("au") == 2
print(sol.lengthOfLongestSubstring("dvdf"))
assert sol.lengthOfLongestSubstring("dvdf") == 3
print(sol.lengthOfLongestSubstring("abba"))
assert sol.lengthOfLongestSubstring("abba") == 2
print(sol.lengthOfLongestSubstring("aab"))
assert sol.lengthOfLongestSubstring("aab") == 2
print(sol.lengthOfLongestSubstring("abcabcbb"))
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
print(sol.lengthOfLongestSubstring("abcdefghijklmnopqrs"))
assert(sol.lengthOfLongestSubstring("abcdefghijklmnopqrs")) == 19