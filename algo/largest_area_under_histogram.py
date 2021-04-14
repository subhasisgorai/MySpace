'''
    Note that we need to deal with the end boundary. We can just add a height 0 to the end of heights 
    which can make sure that all previous heights were checked when we end the for loop.
    Refer here: https://medium.com/techtofreedom/algorithms-for-interview-2-monotonic-stack-462251689da8
'''


def largest_rectangle_area(heights):
    stack, ans = list(), 0
    heights.append(0)
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            curr_height = heights[stack.pop()]
            if stack:
                length = i - stack[-1] - 1
            else:
                length = i
            ans = max(ans, curr_height * length)       
        stack.append(i)
    return ans


if __name__ == '__main__':
    heights = [1, 0, 2, 1, 1, 1, 2]
    print largest_rectangle_area(heights)
