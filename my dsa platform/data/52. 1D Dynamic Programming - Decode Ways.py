"""
Problem: Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.
Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2

Example 2:
Input: s = "226"
Output: 3

Example 3:
Input: s = "0"
Output: 0
"""

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        return dp[n]
