

results = list()


def _prepare_results(building_heights):
    if building_heights:
        stack = list()
        for i, h in enumerate(building_heights):
            while stack and building_heights[stack[-1]] < h:
                stack.pop()
            results.append(stack[-1] if stack else -1)
            stack.append(i)
        return results

    
def can_building_view_sunset(building_heights, building_idx):
    if (building_heights and 
            0 <= building_idx < len(building_heights)):
        if not results:
            _prepare_results(building_heights)
        
        return results[building_idx] == -1


if __name__ == '__main__':
    building_heights = [5, 4, 3, 2, 1]
    print 'can view sunset from {}th building: {}'.format(2,
                                    can_building_view_sunset(building_heights, 2)) 
    print 'can view sunset from {}th building: {}'.format(0,
                                    can_building_view_sunset(building_heights, 0))
    
    del results[:]
    
    building_heights = [2, 3, 5, 1, 7, 2]
    can_see_sunset = [i for i in range(len(building_heights)) 
                            if can_building_view_sunset(building_heights, i)]
    
    print 'Sunset view from these building {}'.format(can_see_sunset)
