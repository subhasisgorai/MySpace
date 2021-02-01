from collections import namedtuple

DailyRecord = namedtuple('DailyRecord', ('temperature', 'day_index'))


def days_to_warmer_day(temperature_arr):
    if temperature_arr:
        stack = list()
        result_arr = [None] * len(temperature_arr)
        for i in range(len(temperature_arr) - 1, -1, -1):
            while (stack and 
                        stack[-1].temperature <= temperature_arr[i]):
                stack.pop()
            result_arr[i] = 0 if not stack else (stack[-1].day_index - i)
            stack.append(DailyRecord(temperature_arr[i], i))
        return result_arr

    
def days_to_warmer_day_without_struct(temperature_arr):
    if temperature_arr:
        stack = list()
        result_arr = [None] * len(temperature_arr)
        for i in range(len(temperature_arr) - 1, -1, -1):
            while (stack and temperature_arr[stack[-1]] <= temperature_arr[i]):
                stack.pop()
            result_arr[i] = 0 if not stack else stack[-1] - i
            stack.append(i)
        return result_arr

    
if __name__ == '__main__':
    temperature_arr = [73, 74, 75, 71, 69, 72, 76, 73]
    print days_to_warmer_day(temperature_arr)
    print days_to_warmer_day_without_struct(temperature_arr)
