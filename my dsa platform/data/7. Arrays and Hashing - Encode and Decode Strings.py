"""
Problem: Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string and decode it back to the list of strings.

Example 1:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Example 2:
Input: ["hello","world"]
Output: ["hello","world"]

Note:
You may assume that all input strings are ASCII characters.
"""

class Solution:
    def encode(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
