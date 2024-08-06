# BiologicalCalculation
a git repo for Biological Calculation course program

# Prerequisites:
Ensure you have Python installed. This script uses Python’s standard libraries and the tabulate library. Install tabulate using pip if it's not already installed:
"pip install tabulate"

# Running the Program:
1. Save the Script: Save the provided Python script as main.py.
2. Run the Script: Execute the script using Python:
   "python main.py"
3.Check Output: After running the script, it will generate a CSV file named gene_outputs.csv in the same directory as the script.
 This file contains the output table, showing the results of the functions for each gene.
The program will also print the functions and filtered functions to the console.

# program description:
Explanation:
This program generates and evaluates functions based on the given states and outputs. 
Each function maps pairs of activator and repressor states to binary outputs (0 or 1). 

The program performs the following tasks:
* Generate Functions: It creates all possible functions that map each pair of activator and repressor states to a binary output.
* Filter Functions: It filters functions based on the following criteria:
* Monotonic Increasing: The output should not decrease as the activator state increases.
* Monotonic Decreasing: The output should not increase as the repressor state increases.
* Condition Compliance: Functions must return 1 for all activators set to "All" and repressors set to "None", and return 0 for all activators set to "None" and repressors set to "All".
* Evaluate Functions for Genes: For each gene, it checks if the gene's activator and repressor states match the function's conditions and records the corresponding output.
* Generate and Save Output: It generates a table of outputs for each function and gene, and saves this table to a CSV file.
