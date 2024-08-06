from itertools import product
from tabulate import tabulate
import csv

"""
States of gene expression and
Possible output values (using boolean representation)
"""
states = ['None', 'Some', 'All']
outputs = ["1", "0"] 

class Gene:
    """
    Represents a gene with activators and inhibitors
    """
    def __init__(self, name, activators_state, inhibitors_state):
        """
        Initialize a Gene object

        :param name: Unique identifier for the gene
        :param activators_state: State of activators (None, Some, or All)
        :param inhibitors_state: State of inhibitors (None, Some, or All)
        """
        self.name = name
        self.activators = activators_state
        self.inhibitors = inhibitors_state

def generate_functions():
    """
    Generates all possible combinations of functions based on the given states and outputs.

    Returns:
        functions (list): A list of dictionaries representing the generated functions.
        Each function is a mapping from an input combination to an output value.
    """
    input_combinations = list(product(states, repeat=2))
    output_combinations = list(product(outputs, repeat=len(input_combinations)))
    
    functions = []
    for output_combination in output_combinations:
        function = {}
        for i, input_pair in enumerate(input_combinations):
            function[input_pair] = output_combination[i]
        functions.append(function)
    
    return functions

def print_functions(functions):
    """
    Print all functions.

    Args:
        functions (list): A list of dictionaries representing the functions.
        Each function is a mapping from an input combination to an output value.

    Returns:
        None

    This function iterates over the given list of functions and prints each function's details.
    It prints the function number, the input combination, and the corresponding output value.
    """
    for i, function in enumerate(functions):
        print(f"Function {i+1}:")
        for input_pair, output in function.items():
            print(f"  {input_pair} -> {output}")
        print()


def is_monotonic_increasing(function):
    """
    Check if a given function is monotonically increasing for activators.

    Args:
        function (dict): A dictionary representing a function, where the keys are tuples of activator and repressor states,
        and the values are the corresponding output values.

    Returns:
        bool: True if the function is monotonically increasing for activators, False otherwise.

    This function checks if a given function is monotonically increasing for activators. It does this by iterating over
    each repressor state and then for each activator state, it checks if the output value is less than the previous
    output value. If it finds a case where the output value decreases, it returns False. If it iterates through all
    activator states without finding any decreasing output values, it returns True, indicating that the function is
    monotonically increasing for activators.
    """
  
    for r in states:
        prev_output = None
        for a in states:
            output = function.get((a, r))
            if prev_output is not None and output < prev_output:
                return False
            prev_output = output
    return True

def is_monotonic_decreasing(function):
    """
    Check if a given function is monotonically decreasing for repressors.

    Args:
        function (dict): A dictionary representing a function, where the keys are tuples of activator and repressor states,
        and the values are the corresponding output values.

    Returns:
        bool: True if the function is monotonically decreasing for repressors, False otherwise.

    This function checks if a given function is monotonically decreasing for repressors. It does this by iterating over
    each activator state and then for each repressor state, it checks if the output value is greater than the previous
    output value. If it finds a case where the output value increases, it returns False. If it iterates through all
    repressor states without finding any increasing output values, it returns True, indicating that the function is
    monotonically decreasing for repressors.
    """
    for a in states:
        prev_output = None
        for r in states:
            output = function.get((a, r))
            if prev_output is not None and output > prev_output:
                return False
            prev_output = output
    return True

def meets_conditions(function):
    """
    Check if a given function meets certain conditions.

    Args:
        function (dict): A dictionary representing a function, where the keys are tuples of activator and repressor states,
        and the values are the corresponding output values.

    Returns:
        bool: True if the function meets the conditions, False otherwise.

    This function checks if a given function meets certain conditions. It checks if the function returns '1' for all
    activators "All" and repressors "None", and if it returns '0' for all activators "None" and repressors "All". If the
    function does not meet these conditions, it returns False. Otherwise, it returns True.
    """
    if function.get(('All', 'None')) != '1':
        return False
    
    if function.get(('None', 'All')) != '0':
        return False
    
    return True

def filter_functions(functions):
    """
    Filter a list of functions based on certain conditions.

    Args:
        functions (list): A list of functions to filter. Each function is represented as a dictionary, where the keys
        are tuples of activator and repressor states, and the values are the corresponding output values.

    Returns:
        list: A list of functions that meet the specified conditions.

    This function filters a list of functions based on the following conditions:
    1. The function is monotonically increasing for activators
    2. The function is monotonically decreasing for repressors 
    3. The function meets certain conditions: it returns '1' for all activators "All" and repressors "None", and
    returns '0' for all activators "None" and repressors "All".

    The function iterates over each function in the input list and checks if it meets the specified conditions. If
    a function meets all three conditions, it is added to the filtered_functions list. Finally, the filtered_functions
    list is returned.
    """
    filtered_functions = []
    for function in functions:
        if is_monotonic_increasing(function) and is_monotonic_decreasing(function)and meets_conditions(function):

            filtered_functions.append(function)
    return filtered_functions


def check_genes_in_functions(genes, functions):
    """
    Checks the output of each gene in a list of functions and returns the results in a 2D list.

    Args:
        genes (list): A list of Gene objects representing the genes to check.
        functions (list): A list of dictionaries representing the functions to check against. Each dictionary has keys
        that are tuples of activator and repressor states, and values that are the corresponding output values.

    Returns:
        list: A 2D list of strings where each row represents a function and each column represents a gene. The values
        in the list are the output values for each gene in each function. If a gene-function pair is not found in the
        input list of functions, the value is "N/A".

    This function iterates over each function in the input list of functions and for each function, it iterates over each
    gene in the input list of genes. For each gene, it retrieves the activator and repressor states and creates an input
    pair. It then checks if the input pair is in the current function dictionary and if so, it retrieves the output value.
    If the input pair is not found in the function dictionary, it uses the default value "N/A". The output value is then
    appended to the current row list. Finally, the row list is appended to the output_data list. The output_data list is
    returned at the end of the function.
    """
    output_data = []
    counter = 0
    for function in functions:
        row = []
        row.append(f"Function {counter}")
        for gene in genes:
            activator_State = gene.activators
            inhibitor_State = gene.inhibitors
            input_pair = (activator_State, inhibitor_State)
            output = function.get(input_pair, "N/A")  # Use "N/A" if the pair is not found
            row.append(output)
        counter= counter+1
        output_data.append(row)
    return output_data


def save_to_csv(headers, rows, filename="gene_outputs.csv"):
    """
    Saves data to a CSV file.

    Args:
        headers (list): A list of column headers.
        rows (list): A list of rows to be written to the CSV file.
        filename (str, optional): The name of the CSV file. Defaults to "gene_outputs.csv".

    Returns:
        None
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

def print_gene_outputs(genes, gene_outputs):
    """
    Prints the outputs of genes in a tabular format and saves the data to a CSV file.

    Args:
        genes (list): A list of Gene objects representing the genes.
        gene_outputs (list): A list of lists representing the outputs of each gene in each function.

    Returns:
        None

    This function generates the headers for the table based on the number of genes. It then saves the data to a CSV file
    using the `save_to_csv` function. Finally, it prints the data in a tabular format using the `tabulate` function.
    """
    headers = ["Function"] + [f"Gene{i+1}" for i in range(len(genes))]
    save_to_csv(headers, gene_outputs)  # Save to CSV
    print(tabulate(gene_outputs, headers, tablefmt="grid"))

def main():
    functions = generate_functions()
    filtered_functions = filter_functions(functions)
    
    for i, function in enumerate(functions):
        print(f"Function {i+1}:")
        for input_pair, output in function.items():
            print(f"  {input_pair} -> {output}")
        print()
    
    for i, function in enumerate(filtered_functions):
        print(f"Function {i+1}:")
        for input_pair, output in function.items():
            print(f"  {input_pair} -> {output}")
        print()

    counter = 0 
    genes = []
    for activator_state in states:
        for inhibitor_state in states:
            gene = Gene(counter, activator_state, inhibitor_state)
            genes.append(gene)
            counter += 1

    # Check genes in functions and get outputs
    gene_outputs = check_genes_in_functions(genes, filtered_functions)
    
    # Print table of gene outputs and save to CSV
    print_gene_outputs(genes, gene_outputs)

if __name__ == "__main__":
    main()