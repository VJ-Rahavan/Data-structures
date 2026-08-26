from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_q = deque(sandwiches)
        student_q = deque(students)
        count = 0

        while count != len(student_q):
            if student_q[0] == sandwich_q[0]:
                student_q.popleft()
                sandwich_q.popleft()
                count = 0
            else:
                front_student = student_q.popleft()
                student_q.append(front_student)
                count += 1
        
        return count
        
