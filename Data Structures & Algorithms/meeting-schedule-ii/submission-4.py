"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=[]
        end=[]
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        count=0
        s,e=0,0 
        ans=0
        while e<len(end) and s<len(start):
            if end[e]>start[s]:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            ans =max(ans,count)
        return ans

