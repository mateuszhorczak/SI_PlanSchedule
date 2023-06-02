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
        self.pe = 3  # wf
        self.education_for_safety = 1
        self.tutoring_hour = 1


class GeneticAlgorithm:
    def __init__(self, population_size):
        self.population_size = population_size

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
                    day = random.choice(days)
                    hour = random.choice(hours)
                    if schedule[day][hour] == "*":
                        schedule[day][hour] = subject
                        break
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
        fitness = 10 * break_time + 400 * break_between_the_same_subject + 100 * (max_school_day_length - optimal_hours_day)

        return [break_time, break_between_the_same_subject, max_school_day_length, fitness]

    def perform_crossover(self, parent1, parent2):
        # operacje krzyzowania na tablicy chromosomow
        crossover_point = random.randint(0, len(parent1))

        child = parent1[:crossover_point] + parent2[crossover_point:]
        print(child)
        return child



    def perform_mutation(self):
        # operacje mutacji na tablicy chromosomow
        pass


if __name__ == '__main__':
    best_score = [0, 0, 0, 99999]
    solutions = []
    best_schedule = {}

    # generate solutions
    for _ in range(10000):
        genetic_algorithm = GeneticAlgorithm(population_size=100)
        school_schedule = genetic_algorithm.generate_initial_population()
        fitness_score = genetic_algorithm.perform_selection(school_schedule)
        solutions.append((school_schedule, fitness_score))

    solutions.sort(reverse=False, key=lambda x: x[1][3])
    best_solutions = solutions[:10]

    for solution in best_solutions:
        for day_name, subjects in solution[0].items():
            print(day_name + ': ' + str(subjects))
        print(f'Ilosc okienek: {solution[1][0]}')
        print(f'Przerwy w przedmiotach: {solution[1][1]}')
        print(f'Najwiecej godzin: {solution[1][2]}')
        print(f'Wynik fitness: {solution[1][3]}')

        # if fitness_score[3] < best_score[3]:
        #     best_score = fitness_score
        #     best_schedule = school_schedule

    # print(f'ilosc okienek: {best_score[0]}')
    # print(f'ilosc dlugich przerw miedzy tymi samymi przedmiotami w ciagu dnia: {best_score[1]}')
    # print(f'najdluzszy czas w szkole: {best_score[2]}')
    # print(f'Fitness score: {best_score[3]}')
    # # reszta logiki i dzialania algorytmu genetycznego
    # for school_day, school_subjects in best_schedule.items():
    #     print(school_day, school_subjects)
