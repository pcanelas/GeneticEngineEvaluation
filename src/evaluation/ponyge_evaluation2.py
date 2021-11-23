import subprocess
import logging
import os 
import shutil

# Configuration variables
PONYGE_PATH = 'PonyGE2/'

ponyge_examples = {
    # Examples
    'pymax': 'parameters/pymax.txt',
    'vectorial': None, # TODO: Not implemented
    'regression': 'parameters/regression.txt',
    'santafe': None, # TODO: Not implemented
    'string_match': 'parameters/string_match.txt',
    'seed_run_target': 'parameters/seed_run_target.txt',
    'GE_parse': 'parameters/GE_parse.txt',
    # Progsys
    'number_io': None,
    'median': None,
    'smallest': None,
    'sum_of_squares': None,
}

# Function to evaluate PonyGE
def evaluate_ponyge2(examples):
        
    if len(examples) > 0:
        run_examples = dict([(name, function) for name, function in ponyge_examples.items() if name in examples])

    else:
        run_examples = ponyge_examples

    for name, parameter_path in run_examples.items():        
        
        logging.info(f"PonyGE: Executing the example: {name}")

        # Write the header of the times file
        f = open("results/ponyge/temp_times.csv", "w")
        f.write("processing_time,evolution_time")
        f.close()

        # Collect the path
        filepath = PONYGE_PATH + 'src/ponyge_eval.py'
        parameter_path = PONYGE_PATH + parameter_path


        # Run 30 times with 30 different seeds
        for seed in range(10):
            subprocess.call(["python3.9", filepath, 
                             '--parameters', parameter_path, 
                             '--random_seed', str(seed),])
        
        os.rename('results/ponyge/temp_times.csv', f'results/ponyge/{name}.csv')
        shutil.rmtree(f'results/ponyge/{name}')