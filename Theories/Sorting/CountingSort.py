"""
Counting Sort: Theory and Implementation
"""

def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    for number in arr:
        count[number - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for number in reversed(arr):
        output[count[number - min_val] - 1] = number
        count[number - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr

'''
Use Cases:
- Sorting integers in a known, small range
- Radix sort subroutine
- Frequency counting
- Data analysis (histograms)
'''
