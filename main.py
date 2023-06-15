# source: https://strefaedukacji.pl/przedmioty-w-liceum-wykaz-i-wymiar-godzin-w-konkretnych-klasach-tego
# -nastolatkowie-ucza-sie-klasach-14-szkoly-ponadpodstawowej/ar/c5-16785765
import math
import random


class FirstClass:  # mat-fiz for example, so +2 to each
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


class ClassRoom:
    def __init__(self, name):
        self.name = name
        days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        hours = list(range(12))  # 12 godzin lekcyjnych w ciagu dnia
        self.schedule = {day: [] for day in days}
        schedule_array = []
        for i in range(12):
            schedule_array.append(Lesson('*', '*', '*'))
        for day in self.schedule:
            self.schedule.update({day: schedule_array})


class Teacher:
    def __init__(self, name):
        self.name = name
        days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        hours = list(range(12))  # 12 godzin lekcyjnych w ciagu dnia
        self.schedule = {day: [] for day in days}
        schedule_array = []
        for i in range(12):
            schedule_array.append(Lesson('*', '*', '*'))
        for day in self.schedule:
            self.schedule.update({day: schedule_array})


class StudentsClass:
    def __init__(self, name):
        self.name = name
        days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        hours = list(range(12))  # 12 godzin lekcyjnych w ciagu dnia
        self.schedule = {day: [] for day in days}
        schedule_array = []
        for i in range(12):
            schedule_array.append(Lesson('*', '*', '*'))
        for day in self.schedule:
            self.schedule.update({day: schedule_array})


class Lesson:
    def __init__(self, name, teacher, classroom):
        self.name = name
        self.teacher = teacher
        self.classroom = classroom


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
        for result_solution in result_solutions:
            result_schedule = list(result_solution[0].students_class.schedule.values())
            day_width = 30

            result_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            for i, result_day in enumerate(result_days):
                fix_subject_view = day_width - len(result_day)
                result_days[i] = result_days[i] + ' ' * fix_subject_view

            for result_day in result_schedule:
                for i, result_subject in enumerate(result_day):
                    fix_subject_view = day_width - len(result_subject)
                    result_day[i] = result_day[i] + ' ' * fix_subject_view

            print('-' * (5 * day_width + 16))
            print(f'| {result_days[0]} | {result_days[1]} | {result_days[2]} | {result_days[3]} | {result_days[4]} |')
            print('-' * (5 * day_width + 16))
            for i in range(12):
                print(f'| {result_schedule[0][i]} | {result_schedule[1][i]} | {result_schedule[2][i]} | '
                      f'{result_schedule[3][i]} | {result_schedule[4][i]} |')
                print('-' * (5 * day_width + 16))

    def generate_initial_population(self):
        # generowanie populacji poczatkowej i wypelnienie tablicy chromosomow
        selected_class = FirstClass()

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
            "tutoring_hour": selected_class.tutoring_hour
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

                    if self.students_class.schedule[rand_day][rand_hour].name == '*' and \
                            rand_classroom.schedule[rand_day][rand_hour].classroom == '*' and \
                            rand_teacher.schedule[rand_day][rand_hour].teacher == '*':

                        new_lesson = Lesson(name=subject, classroom=rand_classroom, teacher=rand_teacher)

                        changed_day_schedule = self.students_class.schedule.get(rand_day)
                        changed_day_schedule[rand_hour] = new_lesson
                        self.students_class.schedule.update({rand_day: changed_day_schedule})  # przypisuje do planu klasy
                        for classroom in self.classrooms:
                            if classroom.name == rand_classroom.name:
                                changed_day_schedule = self.classrooms.schedule.get(rand_day)
                                changed_day_schedule[rand_hour] = new_lesson
                                classroom.schedule.update({rand_day: changed_day_schedule})  # przypisuje do planu sal
                                break
                        for teacher in self.teachers:
                            if teacher.name == rand_teacher.name:
                                changed_day_schedule = self.teachers.schedule.get(rand_day)
                                changed_day_schedule[rand_hour] = new_lesson
                                teacher.schedule.update({rand_day: changed_day_schedule})  # przypisuje do planu nauczyciela
                                break
                        break

        if self.mutation_probability >= random.uniform(0, 1):
            school_schedule.perform_mutation(self)

    def perform_selection(self, chromosome):
        # operacje selekcji na tablicy chromosomów
        break_time = 0  # ilosc okienek
        break_between_the_same_subject = 0  # jesli danego dnia jest 2 razy ten sam przedmiot, to niech będzie w ciągu
        max_school_day_length = 0  # maksymalna dlugosc dnia (by byla jak najmniejsza, by rownomierny plan byl)

        # szukanie okienek
        for day, day_schedule in chromosome.items():
            have_lesson_in_this_day = False
            temp_break_time = 0
            for subject in day_schedule:
                if have_lesson_in_this_day is False and subject != Lesson('*', '*',
                                                                          '*'):  # jesli pierwsza lekcja tego dnia
                    have_lesson_in_this_day = True
                if have_lesson_in_this_day is True and subject == Lesson('*', '*',
                                                                         '*'):  # jesli zaczal lekcje i ma okienko
                    temp_break_time += 1  # tymczasowa przerwa (albo koniec zajec albo okienko)
                if temp_break_time > 0 and subject != Lesson('*', '*', '*'):  # stwierdzenie okienka
                    break_time += temp_break_time
                    temp_break_time = 0

        # przedmiot rozrzucony w ciagu dnia zamiast ciagiem
        for day, day_schedule in chromosome.items():
            check_subjects = {}  # jakie przedmioty ile razy w ciagu dnia
            for subject in day_schedule:
                if subject not in check_subjects and subject != Lesson('*', '*', '*'):
                    check_subjects.update({subject: 1})
                elif subject != Lesson('*', '*', '*'):
                    temp = check_subjects.get(subject)
                    check_subjects.update({subject: temp + 1})

            # pesymistyczna ilosc przerw przedmiotow
            for subject, value in check_subjects.items():
                if value > 1:
                    break_between_the_same_subject = break_between_the_same_subject + value - 1

            # wyliczanie takich przerw
            for i, subject in enumerate(day_schedule):
                if subject != Lesson('*', '*', '*') and i != 11:
                    if check_subjects.get(subject) > 1 and subject == day_schedule[i + 1]:
                        break_between_the_same_subject -= 1

        # maksymalna dlugosc dnia szkolnego
        school_days_length = []
        for day, day_schedule in chromosome.items():
            first_lesson = -1
            last_lesson = -1
            for i, subject in enumerate(day_schedule):
                if first_lesson == -1 and subject != Lesson('*', '*', '*'):
                    first_lesson = i
                if first_lesson != -1 and subject != Lesson('*', '*', '*'):
                    last_lesson = i
            school_days_length.append(last_lesson - first_lesson + 1)
        max_school_day_length = max(school_days_length)

        # wyliczenie optymalnej sredniej ilosci godzin w ciagu dnia
        total_hours = 0
        for day, day_schedule in chromosome.items():
            total_hours += sum(1 for subject in day_schedule if subject != Lesson('*', '*', '*'))
        optimal_hours_day = (total_hours / len(chromosome))
        optimal_hours_day = math.ceil(optimal_hours_day)

        # wyliczenie funkcji fitness
        fitness = 10 * break_time + 400 * break_between_the_same_subject + 100 * (
                max_school_day_length - optimal_hours_day)

        return [break_time, break_between_the_same_subject, max_school_day_length, fitness]

    def perform_crossover(self, parent1, parent2):
        # parent1 = parent1_school_schedule.students_class.schedule
        # parent2 = parent2_school_schedule.students_class.schedule
        # operacje krzyzowania na tablicy chromosomow
        crossover_point = random.randint(0, 5)
        empty_lesson = Lesson('*', '*', '*')
        empty_lesson_array = [empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson,
                              empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson, empty_lesson]
        if crossover_point == 0:
            child = parent2
            removed_subjects_during_crossover = []
        elif crossover_point == 1:
            child = parent2
            removed_subjects_during_crossover = child.students_class.schedule.get('monday')
            removed_classrooms_during_crossover = child.classroom.schedule.get('monday')
            removed_teachers_during_crossover = child.teacher.schedule.get('monday')
            child.students_class.schedule.update({'monday': empty_lesson_array})
            child.classroom.schedule.update({'monday': empty_lesson_array})
            child.teacher.schedule.update({'monday': empty_lesson_array})

        elif crossover_point == 2:
            child = parent2
            removed_subjects_during_crossover = child.students_class.schedule.get('monday') \
                                                + child.students_class.schedule.get('tuesday')
            removed_classrooms_during_crossover = child.classroom.schedule.get('monday') \
                                                  + child.classroom.schedule.get('tuesday')
            removed_teachers_during_crossover = child.teacher.schedule.get('monday') \
                                                + child.teacher.schedule.get('teusday')
            child.students_class.schedule.update({'monday': empty_lesson_array, 'tuesday': empty_lesson_array})
            child.classroom.schedule.update({'monday': empty_lesson_array, 'tuesday': empty_lesson_array})
            child.teacher.schedule.update({'monday': empty_lesson_array, 'tuesday': empty_lesson_array})
        elif crossover_point == 3:
            child = parent1
            removed_subjects_during_crossover = child.students_class.schedule.get('thursday') \
                                                + child.students_class.schedule.get('friday')
            removed_classrooms_during_crossover = child.classroom.schedule.get('thursday') \
                                                  + child.classroom.schedule.get('friday')
            removed_teachers_during_crossover = child.teacher.schedule.get('thursday') \
                                                + child.teacher.schedule.get('friday')
            child.students_class.schedule.update({'thursday': empty_lesson_array, 'friday': empty_lesson_array})
            child.classroom.schedule.update({'thursday': empty_lesson_array, 'friday': empty_lesson_array})
            child.teacher.schedule.update({'thursday': empty_lesson_array, 'friday': empty_lesson_array})
        elif crossover_point == 4:
            child = parent1
            removed_subjects_during_crossover = child.students_class.schedule.get('friday')
            removed_classrooms_during_crossover = child.classroom.schedule.get('friday')
            removed_teachers_during_crossover = child.teacher.schedule.get('friday')
            child.students_class.schedule.update({'friday': empty_lesson_array})
            child.classroom.schedule.update({'friday': empty_lesson_array})
            child.teacher.schedule.update({'friday': empty_lesson_array})

        else:
            child = parent1
            removed_subjects_during_crossover = []

        missing_subjects = {}
        for subject in removed_subjects_during_crossover:
            subject_number = 1 if missing_subjects.get(subject) is None else int(missing_subjects.get(subject)) + 1
            missing_subjects.update({subject: subject_number}) if subject != Lesson('*', '*', '*') else None

        # Przydzielanie przedmiotów do planu zajęć
        for subject, hours_per_week in missing_subjects.items():
            for _ in range(hours_per_week):
                while True:
                    rand_day = random.choice(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
                    rand_hour = random.choice(list(range(0, 12)))
                    rand_classroom = random.choice(child.classrooms)
                    rand_teacher = random.choice(child.teachers)

                    if child.students_class.schedule[rand_day][rand_hour] == Lesson('*', '*', '*') and \
                            rand_classroom.schedule[rand_day][rand_hour].classroom == Lesson('*', '*', '*') and \
                            rand_teacher.schedule[rand_day][rand_hour].teacher == Lesson('*', '*', '*'):

                        new_lesson = Lesson(name=subject, classroom=rand_classroom, teacher=rand_teacher)

                        child.students_class.schedule[rand_day][rand_hour] = new_lesson  # przypisuje do planu klasy
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
        chromosome = genome.students_class.schedule

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
                    day_schedule[i] = Lesson('*', '*', '*')
                    while True:
                        rand_day = random.choice(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
                        rand_hour = random.choice(list(range(1, 12)))
                        if muted_chromosome[rand_day][rand_hour] == Lesson('*', '*', '*'):
                            muted_chromosome[rand_day][rand_hour] = muted_gen
                            break
                    score_after_mutation = school_schedule.perform_selection(muted_chromosome)
                    fitness_score_after_mutation = score_after_mutation[3]
                    if fitness_score_before_mutation >= fitness_score_after_mutation:
                        genome.students_class.schedule.update(muted_chromosome)
                    else:
                        return
        return


if __name__ == '__main__':
    all_solutions = []
    number_of_classrooms = 40
    number_of_teachers = 30

    # generate generations
    for generation in range(10):
        best_score = [0, 0, 0, 99999]
        solutions = []
        best_schedule = {}

        # generate solutions
        for _ in range(10):
            list_of_classrooms = []
            for j in range(number_of_classrooms):
                list_of_classrooms.append(ClassRoom(j + 1))
            list_of_teachers = []
            for j in range(number_of_teachers):
                list_of_teachers.append(Teacher(j + 1))
            list_of_students_class = StudentsClass('our first class')

            school_schedule = GeneticAlgorithm(population_size=100, mutation_probability=0.2, crossed_probability=0.5,
                                               classrooms=list_of_classrooms, teachers=list_of_teachers,
                                               students_class=list_of_students_class)
            school_schedule.generate_initial_population()
            fitness_score = school_schedule.perform_selection(school_schedule.students_class.schedule)
            solutions.append([school_schedule, fitness_score])

        solutions.sort(reverse=False, key=lambda x: x[1][3])
        best_solutions = solutions[:10]

        if school_schedule.crossed_probability >= random.uniform(0, 1):
            potential_parent1 = random.choice(best_solutions)
            potential_parent2 = random.choice(best_solutions)
            child_after_crossed = school_schedule.perform_crossover(potential_parent1[0], potential_parent2[0])
            fitness_score = school_schedule.perform_selection(child_after_crossed.students_class.schedule)  # TODO
            solutions.append([child_after_crossed, fitness_score])

        solutions.sort(reverse=False, key=lambda x: x[1][3])
        best_solutions = solutions[:10]

        all_solutions = all_solutions + best_solutions

        all_solutions.sort(reverse=False, key=lambda x: x[1][3])

        school_schedule.print_schedule(all_solutions[:10])

    # for solution in all_solutions[:10]:
    #     for day_name, schedule_day in solution[0].students_class.schedule.items():
    #         print(day_name + ': ' + str(schedule_day))
    #     print(f'Ilosc okienek: {solution[1][0]}')
    #     print(f'Przerwy w przedmiotach: {solution[1][1]}')
    #     print(f'Najwiecej godzin: {solution[1][2]}')
    #     print(f'Wynik fitness: {solution[1][3]}')
