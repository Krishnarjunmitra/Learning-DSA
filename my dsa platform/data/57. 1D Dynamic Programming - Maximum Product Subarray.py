"""
Problem: Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product, and return the product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6

Example 2:
Input: nums = [-2,0,-1]
Output: 0
"""

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_prod = min_prod = result = nums[0]
        for n in nums[1:]:
            candidates = (n, max_prod * n, min_prod * n)
            max_prod = max(candidates)
            min_prod = min(candidates)
            result = max(result, max_prod)
        return result
