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


class GeneticAlgorithm:
    def __init__(self, population_size, mutation_probability, crossed_probability):
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.crossed_probability = crossed_probability

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

        schedule = {day: ["*"] * len(hours) for day in days}

        # Przydzielanie przedmiotów do planu zajęć
        for subject, hours_per_week in subjects.items():
            for _ in range(hours_per_week):
                while True:
                    rand_day = random.choice(days)
                    rand_hour = random.choice(hours)
                    if schedule[rand_day][rand_hour] == "*":
                        schedule[rand_day][rand_hour] = subject
                        break
        if self.mutation_probability >= random.uniform(0, 1):
            muted_schedule_values = genetic_algorithm.perform_mutation(schedule)
            schedule.update(muted_schedule_values)
        return schedule

    def perform_selection(self, chromosome):
        # operacje selekcji na tablicy chromosomów
        break_time = 0  # ilosc okienek
        break_between_the_same_subject = 0  # jesli danego dnia jest 2 razy ten sam przedmiot, to niech będzie w ciągu
        max_school_day_length = 0  # maksymalna dlugosc dnia (by byla jak najmniejsza, by rownomierny plan byl)

        # szukanie okienek
        for day, day_schedule in chromosome.items():
            have_lesson_in_this_day = False
            temp_break_time = 0
            for lesson_hour in day_schedule:
                if have_lesson_in_this_day is False and lesson_hour != '*':  # jesli pierwsza lekcja tego dnia
                    have_lesson_in_this_day = True
                if have_lesson_in_this_day is True and lesson_hour == '*':  # jesli zaczal lekcje i ma okienko
                    temp_break_time += 1  # tymczasowa przerwa (albo koniec zajec albo okienko)
                if temp_break_time > 0 and lesson_hour != '*':  # stwierdzenie okienka
                    break_time += temp_break_time
                    temp_break_time = 0

        # przedmiot rozrzucony w ciagu dnia zamiast ciagiem
        for day, day_schedule in chromosome.items():
            check_subjects = {}  # jakie przedmioty ile razy w ciagu dnia
            for lesson_hour in day_schedule:
                if lesson_hour not in check_subjects and lesson_hour != '*':
                    check_subjects.update({lesson_hour: 1})
                elif lesson_hour != '*':
                    temp = check_subjects.get(lesson_hour)
                    check_subjects.update({lesson_hour: temp + 1})

            # pesymistyczna ilosc przerw przedmiotow
            for subject, value in check_subjects.items():
                if value > 1:
                    break_between_the_same_subject = break_between_the_same_subject + value - 1

            # wyliczanie takich przerw
            for i, lesson_hour in enumerate(day_schedule):
                if lesson_hour != '*' and i != 11:
                    if check_subjects.get(lesson_hour) > 1 and lesson_hour == day_schedule[i + 1]:
                        break_between_the_same_subject -= 1

        # maksymalna dlugosc dnia szkolnego
        school_days_length = []
        for day, day_schedule in chromosome.items():
            first_lesson = -1
            last_lesson = -1
            for i, lesson_hour in enumerate(day_schedule):
                if first_lesson == -1 and lesson_hour != '*':
                    first_lesson = i
                if first_lesson != -1 and lesson_hour != '*':
                    last_lesson = i
            school_days_length.append(last_lesson - first_lesson + 1)
        max_school_day_length = max(school_days_length)

        # wyliczenie optymalnej sredniej ilosci godzin w ciagu dnia
        total_hours = 0
        for day, day_schedule in chromosome.items():
            total_hours += sum(1 for subject in day_schedule if subject != '*')
        optimal_hours_day = (total_hours / len(chromosome))
        optimal_hours_day = math.ceil(optimal_hours_day)

        # wyliczenie funkcji fitness
        fitness = 10 * break_time + 400 * break_between_the_same_subject + 100 * (
                max_school_day_length - optimal_hours_day)

        return [break_time, break_between_the_same_subject, max_school_day_length, fitness]

    def perform_crossover(self, parent1, parent2):
        # operacje krzyzowania na tablicy chromosomow
        crossover_point = random.randint(0, 5)
        if crossover_point == 0:
            child = parent2
            removed_subjects_during_crossover = []
        elif crossover_point == 1:
            child = parent2
            removed_subjects_during_crossover = child.get('monday')
            child.update({'monday': ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']})
        elif crossover_point == 2:
            child = parent2
            removed_subjects_during_crossover = child.get('monday') + child.get('tuesday')
            child.update({'monday': ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          'tuesday': ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']})
        elif crossover_point == 3:
            child = parent1
            removed_subjects_during_crossover = child.get('thursday') + child.get('friday')
            child.update({'thursday': ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          'friday': ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']})
        elif crossover_point == 4:
            child = parent1
            removed_subjects_during_crossover = child.get('friday')
            child.update({'friday': ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']})
        else:
            child = parent1
            removed_subjects_during_crossover = []

        missing_subjects = {}
        for subject in removed_subjects_during_crossover:
            subject_number = 1 if missing_subjects.get(subject) is None else int(missing_subjects.get(subject)) + 1
            missing_subjects.update({subject: subject_number}) if subject != '*' else None

        # Przydzielanie przedmiotów do planu zajęć
        for subject, hours_per_week in missing_subjects.items():
            for _ in range(hours_per_week):
                while True:
                    rand_day = random.choice(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
                    rand_hour = random.choice(list(range(0, 12)))
                    if child[rand_day][rand_hour] == "*":
                        child[rand_day][rand_hour] = subject
                        break
        return child

    def perform_mutation(self, chromosome):
        # operacje mutacji na tablicy chromosomow
        muted_chromosome = chromosome
        for day, day_schedule in muted_chromosome.items():
            for i, lesson_hour in enumerate(day_schedule):
                # logika kiedy wystepuje mutacja
                if (i == 11 or day_schedule[i + 1] == '*') \
                        and (i == 0 or day_schedule[i - 1] == '*') and lesson_hour != '*':
                    # ---------
                    score_before_mutation = genetic_algorithm.perform_selection(muted_chromosome)
                    fitness_score_before_mutation = score_before_mutation[3]
                    muted_gen = lesson_hour
                    day_schedule[i] = '*'
                    while True:
                        rand_day = random.choice(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
                        rand_hour = random.choice(list(range(1, 12)))
                        if muted_chromosome[rand_day][rand_hour] == '*':
                            muted_chromosome[rand_day][rand_hour] = muted_gen
                            break
                    score_after_mutation = genetic_algorithm.perform_selection(muted_chromosome)
                    fitness_score_after_mutation = score_after_mutation[3]
                    if fitness_score_before_mutation >= fitness_score_after_mutation:
                        chromosome.update(muted_chromosome)
                    else:
                        return chromosome
        return muted_chromosome


if __name__ == '__main__':
    all_solutions = []
    for generation in range(100):
        best_score = [0, 0, 0, 99999]
        solutions = []
        best_schedule = {}

        # generate solutions
        for _ in range(1000):
            genetic_algorithm = GeneticAlgorithm(population_size=100, mutation_probability=0.2, crossed_probability=0.5)
            school_schedule = genetic_algorithm.generate_initial_population()
            fitness_score = genetic_algorithm.perform_selection(school_schedule)
            solutions.append((school_schedule, fitness_score))

        solutions.sort(reverse=False, key=lambda x: x[1][3])
        best_solutions = solutions[:10]

        if genetic_algorithm.crossed_probability >= random.uniform(0, 1):
            potential_parent1 = random.choice(best_solutions)
            potential_parent2 = random.choice(best_solutions)
            child_after_crossed = genetic_algorithm.perform_crossover(potential_parent1[0], potential_parent2[0])
            fitness_score = genetic_algorithm.perform_selection(child_after_crossed)
            solutions.append((child_after_crossed, fitness_score))

        solutions.sort(reverse=False, key=lambda x: x[1][3])
        best_solutions = solutions[:10]

        all_solutions = all_solutions + best_solutions

        all_solutions.sort(reverse=False, key=lambda x: x[1][3])

    for solution in all_solutions[:10]:
        for day_name, schedule_day in solution[0].items():
            print(day_name + ': ' + str(schedule_day))
        print(f'Ilosc okienek: {solution[1][0]}')
        print(f'Przerwy w przedmiotach: {solution[1][1]}')
        print(f'Najwiecej godzin: {solution[1][2]}')
        print(f'Wynik fitness: {solution[1][3]}')
