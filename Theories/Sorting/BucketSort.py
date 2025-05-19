"""
Bucket Sort: Theory and Implementation
"""

def bucket_sort(arr):
    if not arr:
        return arr
    bucket_count = len(arr)
    min_val, max_val = min(arr), max(arr)
    bucket_size = (max_val - min_val) / bucket_count + 1
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        idx = int((num - min_val) / bucket_size)
        buckets[idx].append(num)
    arr.clear()
    for bucket in buckets:
        arr.extend(sorted(bucket))
    return arr

'''
Use Cases:
- Sorting uniformly distributed data
- Floating point numbers
- Distribution sort
'''
