from collections import namedtuple
student_number = int(input())
student = namedtuple("student" ,input().strip().split())
list = [student(*input().strip().split()) for _ in range(student_number)]
print(sum(int(s.MARKS)for s in list)/student_number)