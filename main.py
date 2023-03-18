class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def courses_rate(self, lecturer, course, grade):
        if not isinstance(lecturer,
                          Lecturer) or course not in self.courses_in_progress or course not in lecturer.courses_attached:
            return 'Ошибка'
        else:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]

    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}
        '''
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return (sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))) < (
                    sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])))
        else:
            return 'Не является студентом'

    def __gt__(self, other):
        if isinstance(other, Student):
            return (sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))) > (
                    sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), [])))
        else:
            return 'Не является студентом'

    @staticmethod
    def average_course_grade(self, course):
        course_grades = []
        for student in students:
            course_grades.append(student.grades[course])

        def mean(list):
            total_sum = 0
            count = 0
            for sublist in list:
                for num in sublist:
                    total_sum += num
                    count += 1
            mean_value = total_sum / count
            return mean_value

        return mean(course_grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}

    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {sum(sum(self.courses_grades.values(), [])) / len(sum(self.courses_grades.values(), []))}
        '''
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return (sum(sum(self.courses_grades.values(), [])) / len(sum(self.courses_grades.values(), []))) < (sum(
                sum(other.courses_grades.values(), [])) / len(sum(other.courses_grades.values(), [])))
        else:
            return 'Не является лектором'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return (sum(sum(self.courses_grades.values(), [])) / len(sum(self.courses_grades.values(), []))) > (sum(
                sum(other.courses_grades.values(), [])) / len(sum(other.courses_grades.values(), [])))
        else:
            return 'Не является лектором'

    @staticmethod
    def average_course_grade(self, course):
        course_grades = []
        for lecturer in lecturers:
            course_grades.append(lecturer.courses_grades[course])

        def mean(list):
            total_sum = 0
            count = 0
            for sublist in list:
                for num in sublist:
                    total_sum += num
                    count += 1
            mean_value = total_sum / count
            return mean_value

        return mean(course_grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        '''
        return res


first_student = Student('First', 'Student', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
second_student = Student('Second', 'Student', 'your_gender')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']

first_reviewer = Reviewer('First', 'Reviewer')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']
second_reviewer = Reviewer('Second', 'Reviewer')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Git', 9)
second_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Git', 8)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Git', 10)
second_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Git', 8)

first_reviewer.rate_hw(second_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Git', 7)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 7)
first_reviewer.rate_hw(second_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Git', 6)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 8)

first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']
second_lecturer = Lecturer('First', 'Lecturer')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

first_student.courses_rate(first_lecturer, 'Python', 10)
first_student.courses_rate(first_lecturer, 'Git', 10)
second_student.courses_rate(first_lecturer, 'Python', 9)
second_student.courses_rate(first_lecturer, 'Git', 8)
first_student.courses_rate(first_lecturer, 'Python', 10)
first_student.courses_rate(first_lecturer, 'Git', 10)
second_student.courses_rate(first_lecturer, 'Python', 10)
second_student.courses_rate(first_lecturer, 'Git', 8)

first_student.courses_rate(second_lecturer, 'Python', 10)
first_student.courses_rate(second_lecturer, 'Git', 10)
second_student.courses_rate(second_lecturer, 'Python', 8)
second_student.courses_rate(second_lecturer, 'Git', 7)
first_student.courses_rate(second_lecturer, 'Python', 10)
first_student.courses_rate(second_lecturer, 'Git', 10)
second_student.courses_rate(second_lecturer, 'Python', 8)
second_student.courses_rate(second_lecturer, 'Git', 7)

students = (first_student, second_student)
lecturers = (first_lecturer, second_lecturer)

average_students_grade_git = Student.average_course_grade(students, 'Git')
average_lecturers_grade_git = Lecturer.average_course_grade(lecturers, 'Python')

print(f'Средняя оценка студентов на курсе Git: {average_students_grade_git}')
print(f'Средняя оценка лекторов на курсе Git: {average_lecturers_grade_git}')
