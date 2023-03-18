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
                          Lecturer) or course not in self.courses_in_progress or \
                course not in lecturer.courses_attached or grade < 1 or grade > 10:
            return 'Ошибка'
        else:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.average_grade()}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}
        '''
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise Exception('Не является студентом')
        else:
            return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise Exception('Не является студентом')
        else:
            return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise Exception('Не является студентом')
        else:
            return self.average_grade() == other.average_grade()

    def average_grade(self):
        if not self:
            return 0
        else:
            grades_storage = []
            for grade in self.grades.values():
                grades_storage.extend(grade)
            return round(sum(grades_storage) / len(grades_storage), 2)

    def average_course_grade(persons, course):
        if not isinstance(persons, list):
            return 'Not list'
        course_grades_storage = []
        for person in persons:
            course_grades_storage.extend(person.grades.get(course, []))
        if not course_grades_storage:
            return 'По такому курсу ни у кого оценок нет'
        return round(sum(course_grades_storage) / len(course_grades_storage), 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_grade()}
        '''
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Не является лектором')
        else:
            return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Не является лектором')
        else:
            return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Не является лектором')
        else:
            return self.average_grade() == other.average_grade()

    def average_grade(self):
        if not self:
            return 0
        else:
            grades_storage = []
            for grade in self.grades.values():
                grades_storage.extend(grade)
            return round(sum(grades_storage) / len(grades_storage), 2)

    def average_course_grade(persons, course):
        if not isinstance(persons, list):
            return 'Not list'
        course_grades_storage = []
        for person in persons:
            course_grades_storage.extend(person.grades.get(course, []))
        if not course_grades_storage:
            return 'По такому курсу ни у кого оценок нет'
        return round(sum(course_grades_storage) / len(course_grades_storage), 2)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and 0 < grade < 11:
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
second_lecturer = Lecturer('Second', 'Lecturer')
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

students = [first_student, second_student]
lecturers = [first_lecturer, second_lecturer]

print(Lecturer.average_course_grade(lecturers, 'Git'))
