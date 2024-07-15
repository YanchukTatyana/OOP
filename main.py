class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f"""
                    Имя: {self.name} 
                    Фамилия: {self.surname}
                    Средняя оценка за домашнее задание: {self.student_rating()}
                    Курсы в процессе обучения: {courses_in_progress_string}
                    Завершенные курсы: {finished_courses_string}"""



    def student_rating(self):
        course_count=0
        average_for_all=0
        for i in self.grades:
            for j in self.courses_in_progress:
                if j==i:
                    summ = 0
                    course_count+=1
                    summ = sum(self.grades[i])
                    average_for_all+=summ
        average_for_all = average_for_all / course_count
        return average_for_all

    def __lt__(self, other):
        return self.student_rating() < other.student_rating()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.courses_attached = []
        self.grades = {}


    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
            self.average_rating = sum(map(sum, self.grades.values())) / grades_count
            result = f"""
                        Имя: {self.name} 
                        Фамилия: {self.surname} 
                        Средняя оценка за лекции: {self.lecturer_rating()}"""
            return result

    def lecturer_rating(self):
        average_for_all = 0
        for i in self.grades:
            for j in self.courses_attached:
                summ = 0
                if j == i:
                    summ = sum(self.grades[i])
                average_for_all += summ
        average_for_all = average_for_all / len(self.grades[i])
        return average_for_all

    def __lt__(self, other):
        return self.lecturer_rating() < other.lecturer_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f"""
                    Имя: {self.name} 
                    Фамилия: {self.surname}"""
        return result




best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_1.finished_courses += ['Введение в программирование']
best_student_2 = Student('Oleg', 'Bondarenko', 'your_gender')
best_student_2.courses_in_progress += ['Python', 'Git']
best_student_2.finished_courses += ['Введение в программирование']


best_lecturer_1 = Lecturer('Some', 'Buddy')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Semen', 'Zhdanov')
best_lecturer_2.courses_attached += ['Git']


cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_2 = Reviewer('Semen', 'Zhdanov')
cool_reviewer_2.courses_attached += ['Git']

best_student_1.rate_hw(best_lecturer_1, 'Python', 8)
best_student_1.rate_hw(best_lecturer_2, 'Git', 9)
best_student_2.rate_hw(best_lecturer_1, 'Python', 10)
best_student_2.rate_hw(best_lecturer_2, 'Git', 10)

cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_1.rate_hw(best_student_2, 'Python', 7)
cool_reviewer_2.rate_hw(best_student_1, 'Git', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Git', 10)

print(best_student_1)
print(best_student_2)
print(f'Результат сравнения студентов по средней оценке за домащнее задание:{best_student_1.name} {best_student_1.surname} < {best_student_2.name} {best_student_2.surname} ={best_student_1 > best_student_2}')
print(best_lecturer_1)
print(best_lecturer_2)
print(f'Результат сравнения лекторов по проведенным лекциям:{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 < best_lecturer_2}')
print(cool_reviewer_1)
print(cool_reviewer_2)
