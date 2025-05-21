"""
67. Bit Manipulation - Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: n = 43261596 (00000010100101000001111010011100)
Output: 964176192 (00111001011110000010100101000000)

Example 2:
Input: n = 4294967293 (11111111111111111111111111111101)
Output: 3221225471 (10111111111111111111111111111111)

Constraints:
- The input must be a binary string of length 32
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
