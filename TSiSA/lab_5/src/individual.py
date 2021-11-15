import random


def get_random_binary(bit_capacity: int):
    binary = ""
    for i in range(bit_capacity):
        binary += str(random.randint(0, 1))
    return binary


def decode_gene(gene):
    decoded = 0
    for i in range(len(gene)):
        decoded += int(gene[len(gene) - 1 - i]) * (2 ** i)
    return decoded / ((2 ** len(gene)) - 1)


number_of_genes = 2

class Individual:

    _chromosome = None
    _bits_per_gene = None

    def __init__(self, chromosome: str, bits_per_gene: int):
        self._chromosome = chromosome
        self._bits_per_gene = bits_per_gene

    @classmethod
    def child(cls, chromosome: str):
        global number_of_genes
        assert len(chromosome) % number_of_genes == 0
        bits_per_gene = len(chromosome) // number_of_genes
        return cls(chromosome, bits_per_gene)

    @classmethod
    def random(cls, bits_per_gene: int):
        global number_of_genes
        chromosome = ""
        for i in range(number_of_genes):
            chromosome += get_random_binary(bits_per_gene)
        return cls(chromosome, bits_per_gene)

    def decode_chromosome(self, domain: tuple):
        x_domain, y_domain = domain
        x_domain_from, x_domain_to = x_domain
        y_domain_from, y_domain_to = y_domain
        x = x_domain_from + (decode_gene(self._chromosome[:self._bits_per_gene])) \
            * (x_domain_to - x_domain_from)
        y = y_domain_from + (decode_gene(self._chromosome[self._bits_per_gene:])) \
            * (y_domain_to - y_domain_from)
        return x, y

    def get_chromosome(self):
        return self._chromosome

    def get_fitness(self, fitness_function, domain):
        x, y = self.decode_chromosome(domain)
        return fitness_function(x, y)

    def mutate_me(self):
        mutation_bit_index = random.randint(0, len(self._chromosome) - 1)
        mutation_bit = "1" if self._chromosome[mutation_bit_index] == "0" \
                  else "0"
        self._chromosome = f"{self._chromosome[:mutation_bit_index]}" \
                           f"{mutation_bit}" \
                           f"{self._chromosome[mutation_bit_index + 1:]}"




