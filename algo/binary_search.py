from collections import namedtuple
from bisect import bisect_left


def binary_search(data, target, low, high):
    if low > high:
        return False, -1
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True, mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

        
def binary_search_iterative_without_tail_recursion(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == data[mid]:
            return True, mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False, -1


def left_bound(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low 

def right_bound(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] == target:
            low = mid + 1
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return high 

# student searcher: given an array of students with descending GPA with ties  broken on name
#  use library binary search routine to perform a fast search


Student = namedtuple('Student', ('name', 'grade_point_average'))


def comp_gpa(student):
    return (-student.grade_point_average, student.name)


def search_student(students, target, comp_gpa):
    i = bisect_left([comp_gpa(student) for student in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target, i 


if __name__ == '__main__':
    data = [1, 3, 5, 9, 11, 15, 21, 25, 30]
    print binary_search(data, 21, 0, len(data) - 1)
    print binary_search_iterative_without_tail_recursion(data, 199)
    print binary_search_iterative_without_tail_recursion(data, 21)
    students = [ Student('test1', 95.3), Student('test2', 92.7),
                Student('test5', 90.4), Student('test3', 87.3), Student('test4', 85.6) ]
    print search_student(students, Student('test2', 92.7), comp_gpa)
    
    print left_bound([1, 2, 2, 4, 4, 4, 5, 5], 4)
    print right_bound([1, 2, 2, 4, 4, 4, 5, 5], 4)
    
