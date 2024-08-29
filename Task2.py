class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in intervals[1::]:
            if merged[len(merged)-1][1] >= i[0]:
                merged[len(merged)-1][1] = max(merged[len(merged)-1][1], i[1])
            else:
                merged.append(i)
        return merged