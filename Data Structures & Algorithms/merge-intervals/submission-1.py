class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort(key=lambda pair: pair[0])
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            else:
                prev_interval = stack[-1]
            
            if prev_interval[1] >= interval[0]:
                new_interval = [
                    min(interval[0], prev_interval[0]),
                    max(interval[1], prev_interval[1])
                ]
                stack.pop()
                stack.append(new_interval)
            else:
                stack.append(interval)
        
        return stack
