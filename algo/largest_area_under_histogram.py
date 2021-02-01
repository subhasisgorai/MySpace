'''
    Note that we need to deal with the end boundary. We can just add a height 0 to the end of heights 
    which can make sure that all previous heights were checked when we end the for loop.
    Refer here: https://medium.com/techtofreedom/algorithms-for-interview-2-monotonic-stack-462251689da8
'''


def largest_rectangle_area(heights):
    ret = 0
    mono_stack = list()
    heights.append(0)
    for i, v in enumerate(heights):
        while mono_stack and heights[mono_stack[-1]] > v:
            height = heights[mono_stack.pop()]
            if mono_stack:
                length = i - mono_stack[-1] - 1
            else:
                length = i
            ret = max(ret, height * length)
        mono_stack.append(i)
        # print 'monotonic increasing stack: {}'.format(
        #    map(lambda item: heights[item], mono_stack))
    return ret


if __name__ == '__main__':
    heights = [1, 0, 2, 1, 1, 1, 2]
    print largest_rectangle_area(heights)
