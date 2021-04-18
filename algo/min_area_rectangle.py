from collections import defaultdict


def find_min_area_rectangle(points):
    ys_group_by_x = defaultdict(list)
    for x, y in points:
        ys_group_by_x[x].append(y)
    
    last_x = dict()
    ans = float('inf')
    
    for x in sorted(ys_group_by_x):
        ys = ys_group_by_x[x]
        ys.sort()
        for j, y2 in enumerate(ys):
            for i in range(j):
                y1 = ys[i]
                if (y1, y2) in last_x:
                    ans = min(ans, (x - last_x[y1, y2])) * (y2 - y1)
                last_x[y1, y2] = x
    
    return ans if ans < float('inf') else 0


if __name__ == '__main__':
    print find_min_area_rectangle([[1,1],[1,3],[3,1],[3,3],[2,2]])
