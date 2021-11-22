import sys
import logging
from time import perf_counter_ns

import src.evaluation.helper as helper

# Configuration variables
GENETICENGINE_PATH = 'GeneticEngine/'

gengine_examples = {
    # Examples
    'pymax': 'examples/pymax.py',
    'vectorial': 'examples/vectorialgp_example.py',
    'regression': 'examples/regression_example.py',
    'santafe': 'examples/santafe.py',
    'string_match': 'examples/string_match.py',
    # Progsys
    'number_io': 'examples/progsys/Number_IO.py',
    'median': 'examples/progsys/Median.py',
    'smallest': 'examples/progsys/Smallest.py',
    'sum_of_squares': 'examples/progsys/Sum_of_Squares.py',
}

# Function to evaluate the GeneticEngine
def evaluate_geneticengine(examples: list):
    
    if len(examples) > 0:
        run_examples = dict([(name, path) for name, path in gengine_examples.items() if name in examples])

    else:
        run_examples = gengine_examples

    for name, path in run_examples.items():

        logging.info(f"GEngine: Executing the example: {name}")

        # Obtain the path
        example_path = GENETICENGINE_PATH + path

        # Obtain the preprocessing method
        preprocess_method = helper.get_eval_method(example_path, 'preprocess')

        # Obtain the evolution method
        evol_method = helper.get_eval_method(example_path, 'evolve_pop')
        
        # Check the processing time
        processing_time = perf_counter_ns()
        algorithm = preprocess_method()
        processing_time = processing_time - perf_counter_ns()

        # Check the evolution time
        evolution_time = perf_counter_ns()
        evol_method(algorithm)
        evolution_time = evolution_time - perf_counter_ns()

        logging.info(f"Elapsed processing time: {processing_time}")
        logging.info(f"Elapsed evolution time: {evolution_time}")