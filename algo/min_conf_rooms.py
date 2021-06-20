from collections import namedtuple


def min_meeting_rooms_needed(intervals):
    Point = namedtuple('Point', ('time', 'is_start'))
    points = [
        p for interval in intervals
        for p in [Point(interval[0], True), Point(interval[1], False)]
    ]
    
    points.sort(key=lambda point: (point.time, point.is_start))  # in case of a tie, meeting end would get precedence
    
    current_concurrent_meetings, max_concurrent_meetings = 0, 0
    for point in points:
        if point.is_start:
            current_concurrent_meetings += 1
            max_concurrent_meetings = max(current_concurrent_meetings, max_concurrent_meetings)
        else:
            current_concurrent_meetings -= 1
    
    return max_concurrent_meetings
