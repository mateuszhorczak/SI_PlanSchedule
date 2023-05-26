# source: https://strefaedukacji.pl/przedmioty-w-liceum-wykaz-i-wymiar-godzin-w-konkretnych-klasach-tego
# -nastolatkowie-ucza-sie-klasach-14-szkoly-ponadpodstawowej/ar/c5-16785765
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

    def perform_selection(self):
        # operacje selekcji na tablicy chromosomów
        pass

    def perform_crossover(self):
        # operacje krzyzowania na tablicy chromosomow
        pass

    def perform_mutation(self):
        # operacje mutacji na tablicy chromosomow
        pass


if __name__ == '__main__':
    genetic_algorithm = GeneticAlgorithm(population_size=100)
    first_school_schedule = genetic_algorithm.generate_initial_population()
    # reszta logiki i dzialania algorytmu genetycznego
    for school_day, school_subjects in first_school_schedule.items():
        print(school_day, school_subjects)
