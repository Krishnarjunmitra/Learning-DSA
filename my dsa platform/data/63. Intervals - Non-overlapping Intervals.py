"""
59. Intervals - Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0

Constraints:
- 1 <= intervals.length <= 2 * 10^4
- intervals[i].length == 2
- -2 * 10^4 <= starti < endi <= 2 * 10^4
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count
