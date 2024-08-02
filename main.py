import random

class Gene:
       def __init__(self, num_activators, num_inhibitors):
        self.activators = [False] * num_activators
        self.inhibitors = [False] * num_inhibitors

        def set_activators(self, state):
            if state.lower() == "all":
                self.activators = [True] * len(self.activators)
            elif state.lower() == "some":
                num_true = random.randint(1, num_activators - 1)
                self.activators = [True] * num_true + [False] * (num_activators - num_true)
                random.shuffle(self.activators)
            elif state.lower() == "non":
                self.activators = [False] * len(self.activators)
            else:
                raise ValueError("Invalid state. Must be 'all', 'some', or 'non'")

        def set_inhibitors(self, state):
                    if state.lower() == "all":
                        self.inhibitors = [True] * len(self.inhibitors)
                    elif state.lower() == "some":
                        num_true = random.randint(1, num_inhibitors - 1)
                        self.inhibitors = [True] * num_true + [False] * (num_inhibitors - num_true)
                        random.shuffle(self.inhibitors)
                    elif state.lower() == "non":
                        self.inhibitors = [False] * len(self.inhibitors)
                    else:
                        raise ValueError("Invalid state. Must be 'all', 'some', or 'non'")

def main():
    num_activators = 2
    num_inhibitors = 2
    Genes = []

    for activator_state in ["all", "some", "non"]:
        for inhibitor_state in ["all", "some", "non"]:
            gene = Gene(2, 2)
            gene.set_activators(activator_state)
            gene.set_inhibitors(inhibitor_state)
            Genes.add(gene)

regulationsConditions_table = []
    gene_conditions_options = ["No activators", "No inhibirtors", "exists activators", "exists inhibitors" , "all activators", "all inhibitors", "some activators", "some inhibitors", "non activators", "non inhibitors"]:
    for gene in Genes:
    


if __name__ == "__main__":
    main()