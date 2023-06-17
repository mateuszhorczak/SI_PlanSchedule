# source: https://strefaedukacji.pl/przedmioty-w-liceum-wykaz-i-wymiar-godzin-w-konkretnych-klasach-tego-nastolatkowie-
# ucza-sie-klasach-14-szkoly-ponadpodstawowej/ar/c5-16785765
import math
import random
import string


class FirstClass:
    def __init__(self):
        self.polish_lang = 4
        self.first_lang = 3
        self.second_lang = 2
        self.philosophy = 1
        self.history = 2
        self.history_and_the_present = 2
        self.geography = 1
        self.biology = 1
        self.chemistry = 1
        self.physics = 3
        self.math = 5
        self.it = 1
        self.pe = 3
        self.education_for_safety = 1
        self.tutoring_hour = 1
        self.entrepreneurship = 0
        self.civics = 0


class SecondClass:
    def __init__(self):
        self.polish_lang = 4
        self.first_lang = 3
        self.second_lang = 2
        self.history = 2
        self.civics = 1
        self.entrepreneurship = 1
        self.geography = 2
        self.biology = 2
        self.chemistry = 2
        self.physics = 3
        self.math = 7
        self.it = 1
        self.pe = 3
        self.tutoring_hour = 1
        self.philosophy = 0
        self.history_and_the_present = 0
        self.education_for_safety = 0


class ThirdClass:
    def __init__(self):
        self.polish_lang = 4
        self.first_lang = 3
        self.second_lang = 2
        self.history = 2
        self.entrepreneurship = 1
        self.geography = 1
        self.biology = 1
        self.chemistry = 1
        self.physics = 7
        self.math = 5
        self.it = 1
        self.pe = 3
        self.tutoring_hour = 1
        self.civics = 0
        self.philosophy = 0
        self.history_and_the_present = 1
        self.education_for_safety = 0


class FourthClass:
    def __init__(self):
        self.polish_lang = 4
        self.first_lang = 3
        self.second_lang = 2
        self.history = 1
        self.physics = 4
        self.math = 5
        self.pe = 3
        self.tutoring_hour = 1
        self.entrepreneurship = 0
        self.civics = 0
        self.philosophy = 0
        self.history_and_the_present = 1
        self.geography = 0
        self.biology = 0
        self.chemistry = 0
        self.it = 0
        self.education_for_safety = 0


class ClassRoom:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

        days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        hours = 12  # 12 godzin lekcyjnych w ciagu dnia
        self.schedule = {day: [] for day in days}
        for day in self.schedule:
            schedule_array = []
            for i in range(hours):
                schedule_array.append(Lesson('*', '*', '*', '*', '*'))
            self.schedule.update({day: schedule_array})


class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.class_tutoring = '*'

        days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        hours = 12  # 12 godzin lekcyjnych w ciagu dnia
        self.schedule = {day: [] for day in days}
        for day in self.schedule:
            schedule_array = []
            for i in range(hours):
                schedule_array.append(Lesson('*', '*', '*', '*', '*'))
            self.schedule.update({day: schedule_array})


class StudentsClass:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.tutor = '*'
        self.class_teachers = {
            'polish_lang': '*',
            'first_lang': '*',
            'second_lang': '*',
            'philosophy': '*',
            'history': '*',
            'history_and_the_present': '*',
            'geography': '*',
            'biology': '*',
            'chemistry': '*',
            'physics': '*',
            'math': '*',
            'it': '*',
            'pe': '*',
            'education_for_safety': '*',
            'tutoring_hour': '*',
            'entrepreneurship': '*',
            'civics': '*'
        }

        days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        hours = 12  # 12 godzin lekcyjnych w ciagu dnia
        self.schedule = {day: [] for day in days}
        for day in self.schedule:
            schedule_array = []
            for i in range(hours):
                schedule_array.append(Lesson('*', '*', '*', '*', '*'))
            self.schedule.update({day: schedule_array})


class Lesson:
    def __init__(self, name, teacher, classroom, day, hour):
        self.name = name
        self.teacher = teacher
        self.classroom = classroom
        self.day = day
        self.hour = hour


class GeneticAlgorithm:
    def __init__(self, population_size, mutation_probability, crossed_probability, classrooms, teachers,
                 students_class):
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.crossed_probability = crossed_probability
        self.classrooms = classrooms
        self.teachers = teachers
        self.students_class = students_class

    def print_schedule(self, result_solutions):
        for number_of_solution, result_solution in enumerate(result_solutions):
            print(f'Rozwiazanie: {number_of_solution + 1}')
            for selected_students_class in result_solution[0].students_class:
                print(f'klasa {selected_students_class.grade}{selected_students_class.name}')
                result_schedule = list(selected_students_class.schedule.values())
                table_width = 30

                result_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                for i, result_day in enumerate(result_days):
                    fix_subject_view = table_width - len(result_day)
                    result_days[i] = result_days[i] + ' ' * fix_subject_view

                for result_day in result_schedule:
                    for i, result_subject in enumerate(result_day):
                        fix_subject_view = table_width - len(str(result_subject.name))
                        result_day[i].name = str(result_day[i].name) + ' ' * fix_subject_view

                print('-' * (5 * table_width + 16))
                print(
                    f'| {result_days[0]} | {result_days[1]} | {result_days[2]} | {result_days[3]} | {result_days[4]} |')
                print('-' * (5 * table_width + 16))
                for i in range(12):
                    classroom_names = [
                        str(result_schedule[k][i].classroom.name) if result_schedule[k][i].classroom != '*' else '*'
                        for k in range(len(result_schedule))]
                    teacher_names = [
                        str(result_schedule[k][i].teacher.name) if result_schedule[k][i].teacher != '*' else '*'
                        for k in range(len(result_schedule))]

                    for k, classroom_name in enumerate(classroom_names):
                        fix_subject_view = table_width - len(classroom_name)
                        classroom_names[k] = classroom_names[k] + ' ' * fix_subject_view

                    for k, teacher_name in enumerate(teacher_names):
                        fix_subject_view = table_width - len(teacher_name)
                        teacher_names[k] = teacher_names[k] + ' ' * fix_subject_view

                    print(
                        f'| {result_schedule[0][i].name} | {result_schedule[1][i].name} | '
                        f'{result_schedule[2][i].name} | {result_schedule[3][i].name} | {result_schedule[4][i].name} |')
                    print(
                        f'| {classroom_names[0]} | {classroom_names[1]} | {classroom_names[2]} | {classroom_names[3]} |'
                        f' {classroom_names[4]} |')
                    print(f'| {teacher_names[0]} | {teacher_names[1]} | {teacher_names[2]} | {teacher_names[3]} |'
                          f' {teacher_names[4]} |')
                    print('-' * (5 * table_width + 16))

    def generate_initial_population(self):
        # generowanie populacji poczatkowej i wypelnienie tablicy chromosomow
        for selected_students_class in self.students_class:
            if selected_students_class.grade == 1:
                selected_class = FirstClass()
            elif selected_students_class.grade == 2:
                selected_class = SecondClass()
            elif selected_students_class.grade == 3:
                selected_class = ThirdClass()
            else:
                selected_class = FourthClass()
            subjects = {
                "polish_lang": selected_class.polish_lang,
                "first_lang": selected_class.first_lang,
                "second_lang": selected_class.second_lang,
                "philosophy": selected_class.philosophy,
                "history": selected_class.history,
                "history_and_the_present": selected_class.history_and_the_present,
                "geography": selected_class.geography,
                "biology": selected_class.biology,
                "chemistry": selected_class.chemistry,
                "physics": selected_class.physics,
                "math": selected_class.math,
                "it": selected_class.it,
                "pe": selected_class.pe,
                "education_for_safety": selected_class.education_for_safety,
                "tutoring_hour": selected_class.tutoring_hour,
                "entrepreneurship": selected_class.entrepreneurship,
                "civics": selected_class.civics
            }

            days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
            hours = list(range(12))  # 12 godzin lekcyjnych w ciagu dnia

            # Przydzielanie przedmiotów do planu zajęć
            for subject, hours_per_week in subjects.items():
                for _ in range(hours_per_week):
                    while True:
                        rand_day = random.choice(days)
                        rand_hour = random.choice(hours)
                        rand_classroom = random.choice(self.classrooms)
                        rand_teacher = random.choice(self.teachers)

                        if selected_students_class.schedule[rand_day][rand_hour].name == '*' and \
                                rand_classroom.schedule[rand_day][rand_hour].classroom == '*' and \
                                rand_teacher.schedule[rand_day][rand_hour].teacher == '*' and \
                                subject in rand_teacher.subjects and \
                                subject in rand_classroom.subjects and \
                                (selected_students_class.class_teachers[subject] == '*' or
                                 selected_students_class.class_teachers[subject] == rand_teacher.name) and \
                                (subject != 'tutoring_hour' or
                                 (subject == 'tutoring_hour' and rand_teacher.class_tutoring == '*')):

                            if selected_students_class.class_teachers[subject] == '*':
                                selected_students_class.class_teachers.update({subject: rand_teacher.name})

                            if subject == 'tutoring_hour':
                                rand_teacher.class_tutoring = f'{selected_students_class.name}' \
                                                              f'{selected_students_class.grade}'
                                selected_students_class.tutor = rand_teacher.name

                            new_lesson = Lesson(name=subject, classroom=rand_classroom, teacher=rand_teacher,
                                                day=rand_day,
                                                hour=rand_hour)

                            selected_students_class.schedule[rand_day][
                                rand_hour] = new_lesson  # przypisuje do planu klasy

                            for classroom in self.classrooms:
                                if classroom.name == rand_classroom.name:
                                    classroom.schedule[rand_day][rand_hour] = \
                                        selected_students_class.schedule[rand_day][rand_hour]
                                    break

                            for teacher in self.teachers:
                                if teacher.name == rand_teacher.name:
                                    teacher.schedule[rand_day][
                                        rand_hour] = new_lesson  # przypisuje do planu nauczyciela
                                    break
                            break

            if self.mutation_probability >= random.uniform(0, 1):
                self.perform_mutation(selected_students_class)

    def perform_selection(self, genome):
        # operacje selekcji na tablicy chromosomów
        school_fitness_score = 0
        # definicja skalarow sluzacych do wyliczenia funkcji fitness
        break_time_scalar = 10
        break_between_the_same_subject_scalar = 400
        day_length_scalar = 100

        chromosome = genome.students_class
        for selected_students_class in chromosome:

            break_time = 0  # ilosc okienek
            break_between_the_same_subject = 0  # jesli danego dnia jest 2 razy ten sam przedmiot, to w ciągu
            max_school_day_length = 0  # maksymalna dlugosc dnia (by byla jak najmniejsza, by rownomierny plan byl)

            # szukanie okienek
            for day, day_schedule in selected_students_class.schedule.items():
                have_lesson_in_this_day = False
                temp_break_time = 0
                for subject in day_schedule:
                    if have_lesson_in_this_day is False and subject.name != '*':  # jesli pierwsza lekcja tego dnia
                        have_lesson_in_this_day = True
                    if have_lesson_in_this_day is True and subject.name == '*':  # jesli zaczal lekcje i ma okienko
                        temp_break_time += 1  # tymczasowa przerwa (albo koniec zajec albo okienko)
                    if temp_break_time > 0 and subject.name != '*':  # stwierdzenie okienka
                        break_time += temp_break_time
                        temp_break_time = 0

            # przedmiot rozrzucony w ciagu dnia zamiast ciagiem
            for day, day_schedule in selected_students_class.schedule.items():
                check_subjects = {}  # jakie przedmioty ile razy w ciagu dnia
                for subject in day_schedule:
                    if subject not in check_subjects and subject.name != '*':
                        check_subjects.update({subject: 1})
                    elif subject.name != '*':
                        temp = check_subjects.get(subject)
                        check_subjects.update({subject: temp + 1})

                # pesymistyczna ilosc przerw przedmiotow
                for subject, value in check_subjects.items():
                    if value > 1:
                        break_between_the_same_subject = break_between_the_same_subject + value - 1

                # wyliczanie takich przerw
                for i, subject in enumerate(day_schedule):
                    if subject.name != '*' and i != 11:
                        if check_subjects.get(subject) > 1 and subject == day_schedule[i + 1]:
                            break_between_the_same_subject -= 1

            # maksymalna dlugosc dnia szkolnego
            school_days_length = []
            for day, day_schedule in selected_students_class.schedule.items():
                first_lesson = -1
                last_lesson = -1
                for i, subject in enumerate(day_schedule):
                    if first_lesson == -1 and subject.name != '*':
                        first_lesson = i
                    if first_lesson != -1 and subject.name != '*':
                        last_lesson = i
                school_days_length.append(last_lesson - first_lesson + 1)
            max_school_day_length = max(school_days_length)

            # wyliczenie optymalnej sredniej ilosci godzin w ciagu dnia
            total_hours = 0
            for day, day_schedule in selected_students_class.schedule.items():
                total_hours += sum(1 for subject in day_schedule if subject.name != '*')
            optimal_hours_day = (total_hours / len(selected_students_class.schedule))
            optimal_hours_day = math.ceil(optimal_hours_day)

            # wyliczenie funkcji fitness
            fitness = break_time_scalar * break_time + break_between_the_same_subject_scalar * break_between_the_same_subject + day_length_scalar * (
                    max_school_day_length - optimal_hours_day)

            school_fitness_score += fitness

        # wyliczenie okienek nauczycieli
        chromosome = genome.teachers
        for selected_teacher in chromosome:
            break_time = 0  # ilosc okienek

            # szukanie okienek
            for day, day_schedule in selected_teacher.schedule.items():
                have_lesson_in_this_day = False
                temp_break_time = 0
                for subject in day_schedule:
                    if have_lesson_in_this_day is False and subject.name != '*':  # jesli pierwsza lekcja tego dnia
                        have_lesson_in_this_day = True
                    if have_lesson_in_this_day is True and subject.name == '*':  # jesli zaczal lekcje i ma okienko
                        temp_break_time += 1  # tymczasowa przerwa (albo koniec zajec albo okienko)
                    if temp_break_time > 0 and subject.name != '*':  # stwierdzenie okienka
                        break_time += temp_break_time
                        temp_break_time = 0

            # wyliczenie funkcji fitness
            fitness = break_time_scalar * break_time
            school_fitness_score += fitness

        return school_fitness_score

    def perform_crossover(self, parent1, parent2):
        # operacje krzyzowania na tablicy chromosomow
        crossover_point = random.randint(0, 5)
        empty_lesson = Lesson('*', '*', '*', '*', '*')
        empty_lesson_array = [empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson,
                              empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson]

        crossover_class = random.choice(range(len(parent1.students_class)))

        if crossover_point == 0:
            child = parent2
            removed_subjects_during_crossover = []
        elif crossover_point == 1:
            child = parent2
            removed_subjects_during_crossover = child.students_class[crossover_class].schedule.get('monday')
            child.students_class[crossover_class].schedule.update({'monday': empty_lesson_array})
        elif crossover_point == 2:
            child = parent2
            removed_subjects_during_crossover = child.students_class[crossover_class].schedule.get(
                'monday') + child.students_class[crossover_class].schedule.get('tuesday')
            child.students_class[crossover_class].schedule.update({'monday': empty_lesson_array,
                                                                   'tuesday': empty_lesson_array})
        elif crossover_point == 3:
            child = parent1
            removed_subjects_during_crossover = child.students_class[crossover_class].schedule.get(
                'thursday') + child.students_class[crossover_class].schedule.get('friday')
            child.students_class[crossover_class].schedule.update({'thursday': empty_lesson_array,
                                                                   'friday': empty_lesson_array})
        elif crossover_point == 4:
            child = parent1
            removed_subjects_during_crossover = child.students_class[crossover_class].schedule.get('friday')
            child.students_class[crossover_class].schedule.update({'friday': empty_lesson_array})

        else:
            child = parent1
            removed_subjects_during_crossover = []

        for subject in removed_subjects_during_crossover:
            for classroom in child.classrooms:
                if classroom != '*' and subject.classroom != '*' and classroom.name == subject.classroom.name:
                    classroom.schedule[subject.day][subject.hour] = Lesson('*', '*', '*', '*', '*')
                    break
            for teacher in child.teachers:
                if teacher != '*' and subject.classroom != '*' and teacher.name == subject.teacher.name:
                    teacher.schedule[subject.day][subject.hour] = Lesson('*', '*', '*', '*', '*')
                    break

        missing_subjects = {}
        for subject in removed_subjects_during_crossover:
            subject_number = 1 if missing_subjects.get(subject) is None else int(missing_subjects.get(subject)) + 1
            missing_subjects.update({subject: subject_number}) if subject != Lesson('*', '*', '*', '*', '*') else None

        # Przydzielanie przedmiotów do planu zajęć
        for subject, hours_per_week in missing_subjects.items():
            for _ in range(hours_per_week):
                while True:
                    rand_day = random.choice(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
                    rand_hour = random.choice(list(range(0, 12)))
                    rand_classroom = random.choice(child.classrooms)
                    rand_teacher = random.choice(child.teachers)

                    if child.students_class[crossover_class].schedule[rand_day][rand_hour].name == '*' and \
                            rand_classroom.schedule[rand_day][rand_hour].classroom == '*' \
                            and rand_teacher.schedule[rand_day][rand_hour].teacher == '*':

                        new_lesson = Lesson(name=subject.name, classroom=rand_classroom, teacher=rand_teacher,
                                            day=rand_day, hour=rand_hour)

                        child.students_class[crossover_class].schedule[rand_day][
                            rand_hour] = new_lesson  # przypisuje do planu klasy

                        for classroom in child.classrooms:
                            if classroom.name == rand_classroom.name:
                                classroom.schedule[rand_day][rand_hour] = new_lesson  # przypisuje do planu sal
                                break
                        for teacher in child.teachers:
                            if teacher.name == rand_teacher.name:
                                teacher.schedule[rand_day][rand_hour] = new_lesson  # przypisuje do planu nauczyciela
                                break
                        break
        return child

    def perform_mutation(self, genome):
        # operacje mutacji na tablicy chromosomow
        chromosome = genome.schedule

        muted_chromosome = chromosome
        for day, day_schedule in muted_chromosome.items():
            for i, subject in enumerate(day_schedule):
                # logika kiedy wystepuje mutacja
                if (i == 11 or day_schedule[i + 1] == '*') \
                        and (i == 0 or day_schedule[i - 1] == '*') and subject != '*':
                    # ---------
                    score_before_mutation = school_schedule.perform_selection(muted_chromosome)
                    fitness_score_before_mutation = score_before_mutation[3]
                    muted_gen = subject
                    day_schedule[i] = Lesson('*', '*', '*', '*', '*')
                    while True:
                        rand_day = random.choice(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
                        rand_hour = random.choice(list(range(1, 12)))
                        if muted_chromosome[rand_day][rand_hour] == Lesson('*', '*', '*', '*', '*'):
                            muted_chromosome[rand_day][rand_hour] = muted_gen
                            break
                    score_after_mutation = school_schedule.perform_selection(muted_chromosome)
                    fitness_score_after_mutation = score_after_mutation[3]
                    if fitness_score_before_mutation >= fitness_score_after_mutation:
                        genome.schedule.update(muted_chromosome)
                    else:
                        return
        return


if __name__ == '__main__':
    all_solutions = []
    number_of_students_class = 2
    students_class_grades = [1, 2, 3, 4]

    # generate generations
    for generation in range(10):
        best_score = [0, 0, 0, 99999]
        letters = string.ascii_uppercase
        solutions = []
        best_schedule = {}

        # generate solutions
        for _ in range(100):
            list_of_classrooms = [
                ClassRoom(1, ['pe']),
                ClassRoom(2, ['pe']),
                ClassRoom(3, ['it', 'tutoring_hour']),
                ClassRoom(4, ['it']),
                ClassRoom(5, ['it']),
                ClassRoom(6, ['chemistry']),
                ClassRoom(7, ['chemistry', 'biology', 'physics', 'geography']),
                ClassRoom(8, ['chemistry', 'biology', 'physics', 'geography', 'tutoring_hour']),
                ClassRoom(9, ['polish_lang', 'first_lang', 'second_lang', 'philosophy', 'history',
                              'history_and_the_present', 'math', 'tutoring_hour', 'entrepreneurship', 'civics']),
                ClassRoom(10, ['history', 'history_and_the_present', 'tutoring_hour']),
                ClassRoom(11, ['history', 'history_and_the_present', 'tutoring_hour']),
                ClassRoom(12, ['math', 'tutoring_hour']),
                ClassRoom(13, ['math']),
                ClassRoom(14, ['math']),
                ClassRoom(15, ['education_for_safety', 'tutoring_hour']),
                ClassRoom(16, ['entrepreneurship', 'civics', 'polish_lang', 'first_lang', 'second_lang', 'philosophy',
                               'history', 'history_and_the_present', 'tutoring_hour']),
                ClassRoom(17, ['entrepreneurship', 'civics', 'polish_lang', 'first_lang', 'second_lang', 'philosophy',
                               'history', 'history_and_the_present', 'tutoring_hour']),
                ClassRoom(18, ['entrepreneurship', 'civics', 'polish_lang', 'first_lang', 'second_lang', 'philosophy',
                               'history', 'history_and_the_present', 'tutoring_hour']),
                ClassRoom(19, ['entrepreneurship', 'civics', 'polish_lang', 'first_lang', 'second_lang', 'philosophy',
                               'history', 'history_and_the_present', 'tutoring_hour']),
                ClassRoom(20, ['entrepreneurship', 'civics', 'polish_lang', 'first_lang', 'second_lang', 'philosophy',
                               'history', 'history_and_the_present', 'tutoring_hour']),
                ClassRoom(21, ['math']),
                ClassRoom(22, ['math']),
                ClassRoom(23, ['math']),
                ClassRoom(24, ['chemistry', 'biology', 'physics', 'geography', 'tutoring_hour']),
                ClassRoom(25, ['chemistry', 'biology', 'physics', 'geography', 'tutoring_hour']),
            ]

            list_of_teachers = [
                Teacher('Nauczyciel 1', ['tutoring_hour', 'polish_lang', 'philosophy']),
                Teacher('Nauczyciel 2', ['tutoring_hour', 'polish_lang', 'philosophy']),
                Teacher('Nauczyciel 3', ['history', 'polish_lang', 'first_lang']),
                Teacher('Nauczyciel 4', ['tutoring_hour', 'first_lang', 'second_lang']),
                Teacher('Nauczyciel 5', ['tutoring_hour', 'history', 'history_and_the_present']),
                Teacher('Nauczyciel 6', ['tutoring_hour', 'history', 'history_and_the_present']),
                Teacher('Nauczyciel 7', ['polish_lang', 'history', 'history_and_the_present']),
                Teacher('Nauczyciel 8', ['tutoring_hour', 'pe']),
                Teacher('Nauczyciel 9', ['pe']),
                Teacher('Nauczyciel 10', ['pe']),
                Teacher('Nauczyciel 11', ['education_for_safety']),
                Teacher('Nauczyciel 12', ['first_lang']),
                Teacher('Nauczyciel 13', ['second_lang']),
                Teacher('Nauczyciel 14', ['first_lang', 'entrepreneurship']),
                Teacher('Nauczyciel 15', ['tutoring_hour', 'biology', 'chemistry', 'physics']),
                Teacher('Nauczyciel 16', ['tutoring_hour', 'biology', 'chemistry']),
                Teacher('Nauczyciel 17', ['tutoring_hour', 'geography', 'education_for_safety', 'physics']),
                Teacher('Nauczyciel 18', ['tutoring_hour', 'math']),
                Teacher('Nauczyciel 19', ['tutoring_hour', 'math', 'it', 'physics']),
                Teacher('Nauczyciel 20', ['tutoring_hour', 'math', 'it', 'physics']),
                Teacher('Nauczyciel 21', ['tutoring_hour', 'math']),
                Teacher('Nauczyciel 22', ['math']),
                Teacher('Nauczyciel 23', ['civics', 'second_lang']),
                Teacher('Nauczyciel 24', ['tutoring_hour', 'second_lang']),
                Teacher('Nauczyciel 25', ['tutoring_hour', 'math', 'it']),
                Teacher('Nauczyciel 26', ['polish_lang'])
            ]

            list_of_students_class = []
            for j in range(number_of_students_class):
                for grade_class in students_class_grades:
                    list_of_students_class.append(StudentsClass(letters[j], grade_class))

            school_schedule = GeneticAlgorithm(population_size=100, mutation_probability=0.2, crossed_probability=0.5,
                                               classrooms=list_of_classrooms, teachers=list_of_teachers,
                                               students_class=list_of_students_class)
            school_schedule.generate_initial_population()
            fitness_score = school_schedule.perform_selection(school_schedule)
            solutions.append([school_schedule, fitness_score])

        solutions.sort(reverse=False, key=lambda x: x[1])
        best_solutions = solutions[:10]

        if school_schedule.crossed_probability >= random.uniform(0, 1):
            potential_parent1 = random.choice(best_solutions)
            potential_parent2 = random.choice(best_solutions)
            child_after_crossed = school_schedule.perform_crossover(potential_parent1[0], potential_parent2[0])
            fitness_score = school_schedule.perform_selection(child_after_crossed)  # TODO
            solutions.append([child_after_crossed, fitness_score])

        solutions.sort(reverse=False, key=lambda x: x[1])
        best_solutions = solutions[:10]

        all_solutions = all_solutions + best_solutions
        all_solutions.sort(reverse=False, key=lambda x: x[1])
    school_schedule.print_schedule(all_solutions[:1])
