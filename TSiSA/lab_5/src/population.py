import random

from individual import Individual


probability_of_crossover = 1.0
probability_of_mutation  = 0.70


class Population:

    _number_of_individuals = None
    _individuals = None
    _intermediate_population = None
    _fitness_function = None
    _domain = None

    def __init__(self, individuals: list):
        self._number_of_individuals = len(individuals)
        self._individuals = individuals

    def set_fitness_function(self, fitness_function):
        self._fitness_function = fitness_function

    def set_domain(self, domain):
        self._domain = domain

    def check_domain_and_fitness_function(self):
        if not self._domain:
            RuntimeError('domain is not set')
        if not self._fitness_function:
            RuntimeError('fitness function is not set')

    @classmethod
    def initial(cls, number_of_individuals: int, bits_per_gene: int):
        individuals = []
        for i in range(number_of_individuals):
            individuals.append(Individual.random(bits_per_gene))
        return cls(individuals)

    def get_current_generation(self):
        return self._individuals

    def evolve(self):
        assert len(self._individuals) == self._number_of_individuals
        self.check_domain_and_fitness_function()

        self.new_intermediate_population()
        print("population after selection:")
        self.print_chromosomes(self._intermediate_population)
        assert len(self._individuals) == self._number_of_individuals

        self.recombinate()
        print("population after recombination:")
        self.print_chromosomes(self._individuals)
        assert len(self._individuals) == self._number_of_individuals

        self.mutate()
        print("population after mutation:")
        self.print_chromosomes(self._individuals)
        assert len(self._individuals) == self._number_of_individuals

    @staticmethod
    def print_chromosomes(individuals):
        for individual in individuals:
            print(individual.get_chromosome())
        print()
            
    def new_intermediate_population(self):
        self._intermediate_population = []
        marks = self.get_roulette_marks()
        for i in range(self._number_of_individuals):
            self._intermediate_population.append(self.sample(marks))

    def get_roulette_marks(self):
        fitnesses = [individual.get_fitness(self._fitness_function, self._domain) for individual in self._individuals]
        fitnesses_normalized = self.get_fitnesses_normalized_positively(fitnesses)
        fitness_total = sum(fitnesses_normalized)
        assert fitness_total > 0
        marks = []
        for i in range(self._number_of_individuals):
            pass_chance = fitnesses_normalized[i] / fitness_total
            if i == 0:
                marks.append(pass_chance)
                continue
            marks.append(marks[-1] + pass_chance)
        marks[-1] = 1.0
        return marks

    @staticmethod
    def get_fitnesses_normalized_positively(fitnesses):
        min_fit = min(fitnesses)
        fitnesses_normalized = [fitness - min_fit for fitness in fitnesses]
        return fitnesses_normalized

    def sample(self, marks):
        assert len(marks) == len(self._individuals)
        throw = random.random()
        for i in range(len(marks)):
            if throw <= marks[i]:
                return self._individuals[i]
        assert False

    def recombinate(self):
        couples = self.encouple_intermediate_population()
        new_generation = []
        for mother, father in couples:
            if not mother or not father:
                for lonely_wolf in (mother, father):
                    if lonely_wolf:
                        new_generation.append(lonely_wolf)
            if self.do_we_make_crossover():
                bruder, schwester = self.crossover(mother, father)
                for brand_new_one in (bruder, schwester):
                    new_generation.append(brand_new_one)
                continue
            for childfree in (mother, father):
                new_generation.append(childfree)
        self._individuals = new_generation

    def encouple_intermediate_population(self) -> list:
        assert len(self._intermediate_population) == self._number_of_individuals
        couples = []
        individuals = self._intermediate_population
        random.shuffle(individuals)
        if len(individuals) % 2 == 1:
            couples += (individuals.pop(-1), None)
        while individuals:
            couples.append((individuals.pop(-1), individuals.pop(-1)))
        return couples

    @staticmethod
    def do_we_make_crossover() -> bool:
        global probability_of_crossover
        return random.random() < probability_of_crossover

    @staticmethod
    def crossover(mother: Individual, father: Individual) -> tuple:
        mother_chromosome = mother.get_chromosome()
        father_chromosome = father.get_chromosome()
        assert len(mother_chromosome) == len(father_chromosome)
        separator = random.randint(0, len(mother_chromosome) - 1)
        bruder_chromosome    = mother_chromosome[:separator] + father_chromosome[separator:]
        schwester_chromosome = father_chromosome[:separator] + mother_chromosome[separator:]
        return Individual.child(bruder_chromosome), Individual.child(schwester_chromosome)

    def mutate(self):
        for i in range(len(self._individuals)):
            if self.im_lucky_to_mutate():
                self._individuals[i].mutate_me()

    @staticmethod
    def im_lucky_to_mutate() -> bool:
        global probability_of_mutation
        return random.random() < probability_of_mutation





