"""
Problem: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "bbbbb"
Output: 1

Example 3:
Input: s = "pwwkew"
Output: 3
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_len = 0
        for right, c in enumerate(s):
            if c in char_index and char_index[c] >= left:
                left = char_index[c] + 1
            char_index[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len
