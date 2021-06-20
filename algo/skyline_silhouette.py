from sortedcontainers import SortedSet
from collections import namedtuple


def get_skyline_silhouette(buildings):
    Building = namedtuple('Building', ('start', 'end', 'height'))
    EndPoint = namedtuple('EndPoint', ('x', 'y', 'is_start', 'building'))
    if buildings:
        buildings = [Building(b[0], b[1], b[2]) for b in buildings if b and len(b) == 3]
        points = [
                point for building in buildings 
                for point in (EndPoint(building.start, building.height, True, building),
                              EndPoint(building.end, building.height, False, building))
            ]
        
        points.sort(key=lambda p: (p.x, not p.is_start, -p.y))
        sorted_set = SortedSet(key=lambda b:-b.height)
        
        result, current_height = list(), 0
        for point in points:
            if point.is_start:
                if point.y > current_height:
                    current_height = point.y
                    result.append([point.x, point.y])
                sorted_set.add(point.building)
            else:
                if point.building in sorted_set:
                    sorted_set.remove(point.building)
                new_height = sorted_set[0].height if sorted_set else 0
                if current_height != new_height:
                    current_height = new_height
                    if result[-1][0] == point.x:
                        result.pop()
                    result.append([point.x, current_height])
        
        return result
        