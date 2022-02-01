import os
import multiprocessing as mp
import src.helper as helper

# Configuration variables
GENETICENGINE_PATH = 'GeneticEngine/'
RESULTS_PATH = './results/treebased_ge_comparison'

def execute_plot(plot_method, file_run_names, run_names, result_name='results/images/medians.pdf', metric='fitness', single_value=False):

    # Check the evolution time
    plot_method(file_run_names, run_names, result_name, metric, single_value)
    

# Function to evaluate the GeneticEngine
def evaluate_geneticengine(example, file_addition=''):

    os.chdir('GeneticEngine/')
    representations = ['treebased_representation','grammatical_evolution']
    folders = [ GENETICENGINE_PATH + RESULTS_PATH + '/' + r for r in representations ]
    output_folder = './results/images/treebased_ge_comparison/'
    helper.create_folder(output_folder)
    
    filepath = GENETICENGINE_PATH + 'geneticengine/visualization/plot_comparison.py'
    
    plot_method = helper.get_eval_method(filepath, 'plot_comparison') 
    
    print(f"Example: {example}.")
    process = mp.Process(target=execute_plot,
                            args=(plot_method,
                                  folders,
                                  representations,
                                  output_folder + f'{example}{file_addition}.pdf'
                                  ))
    process.start()
    process.join()
    helper.copy_folder(output_folder,f'results/treebased_ge_comparison/images/')

    

