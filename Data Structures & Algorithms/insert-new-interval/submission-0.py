from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # 1. Add all intervals *before* the newInterval (intervals[i][1] < newInterval[0])
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # 2. Merge all overlapping intervals
        # Condition: interval's start is before newInterval's end (intervals[i][0] <= newInterval[1])
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update the boundaries of the newInterval
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # 3. Add the single merged interval
        result.append(newInterval)
        
        # 4. Add all intervals *after* the newInterval
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result