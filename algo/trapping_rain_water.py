

def trap_water(heights):
        stack, trapped_water = list(), 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] < height:
                lower_height = heights[stack.pop()]
                if not stack:
                    break
                else:
                    effective_height = min(height, heights[stack[-1]]) - lower_height
                    effective_length = i - stack[-1] - 1
                    trapped_water += effective_height * effective_length
            stack.append(i)
            print 'monotonic decreasing stack: {}'.format(
            map(lambda item: heights[item], stack))
        return trapped_water


if __name__ == '__main__':
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print 'trapped_water: {}'.format(trap_water(heights))
    
    heights = [4, 2, 0, 3, 2, 5]
    print 'trapped_water: {}'.format(trap_water(heights))
