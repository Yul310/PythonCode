class Solution(object):
    def insert(self, intervals, newInterval):



        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        result = []
        for interval in intervals:
            # print(result)
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
                
        return result