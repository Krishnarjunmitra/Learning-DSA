class Solution:
    def is_palindrome(self, s):
        s = ''.join(filter(str.isalnum, str(s))).lower()
        return s == s[::-1]
