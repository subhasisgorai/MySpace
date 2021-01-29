

class Student:

    def __init__(self, name, grade_point_average):
        self.name = name
        self.grade_point_average = grade_point_average
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __str__(self):
        return '[{}, {}]'.format(self.name, self.grade_point_average)
    
    def __repr__(self):
        return self.__str__()
    
    
if __name__ == '__main__':
    students = [
        Student('A', 4.0),
        Student('C', 3.0),
        Student('B', 2.0),
        Student('D', 3.2)
    ]
    
    print sorted(students)
    
    students.sort(key=lambda student: student.grade_point_average)
    print students
