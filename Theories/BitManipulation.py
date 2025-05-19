"""
Bit Manipulation: Theory and Implementation
"""

def count_set_bits(n):
    count = 0
    while n:
        n &= (n-1)
        count += 1
    return count

def is_power_of_two(n):
    return n > 0 and (n & (n-1)) == 0

'''
Use Cases:
- Fast arithmetic operations
- Cryptography
- Compression algorithms
- Graphics and image processing
'''
