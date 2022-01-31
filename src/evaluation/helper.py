from importlib import import_module
from os import listdir
from os.path import isfile, join
import pandas as pd
import os 

def get_eval_method(example_path, method_name):
    example_path = example_path.replace('/', '.')
    mod = import_module(example_path[:-3], 'geneticengine')
    return getattr(mod, method_name)

def create_folder(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass

def import_data(examples, path, mode, delimiter):

    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    
    res = dict()

    for name in examples:
        if f'{name}_{mode}.csv' in onlyfiles:
            res[name] = pd.read_csv(path + f'{name}_{mode}.csv', sep=delimiter)
    
    return res

def write_to_csv_times(times, mode):
    path = 'results/ponyge_comparison/gengine/'
    create_folder(path)

    for name, dataframe in times.items():

        f = open(f"results/ponyge_comparison/gengine/{name}_{mode}.csv", "w")

        if mode == 'generations':
            f.write("processing_time,evolution_time")
            for _, row in dataframe.iterrows():
                f.write(f"\n{row.loc['processing_time']},{row.loc['evolution_time']}")
        
        else:
            f.write("best_fitness")
            for index, row in dataframe.iterrows():
                f.write(f"\n{row.loc['best_fitness']}")
        
        f.close()        