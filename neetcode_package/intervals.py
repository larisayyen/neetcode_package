
def insert(intervals, newInterval):
    '''
    Insert newInterval(list) into intervals(list of list)
    such that intervals is still sorted in ascending order by starti
    and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
    '''
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]

        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])

        else:
            newInterval = [
                min(newInterval[0],intervals[i][0]),
                max(newInterval[1],intervals[i][1])
            ]

        res.append(newInterval)

        return res

def merge(intervals):
    '''
    merge all overlapping intervals
    return an array of the non-overlapping intervals that cover all the intervals in the input.
    '''
    # sort by the start value
    intervals.sort(key = lambda pair:pair[0])

    output = [intervals[0]]

    for start,end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd,end)

        else:
            output.append([start,end])

    return output
