import sys
import src.evaluation.helper as helper

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_df(ponyge_df, gengine_df, example, col_name, mode):
    ponyge_vals = ponyge_df[col_name].values
    gengine_vals = gengine_df[col_name].values

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.violinplot([ponyge_vals, gengine_vals])
    tix = ['PonyGE', 'GeneticEngine']
    plt.xticks([1,2], tix, rotation=0, fontsize=12)
    if mode == 'generations':
        plt.title(f"{col_name.capitalize()} time per Tool")
        ax.set_ylabel("Time (s)", fontsize=12)
    else:
        plt.title(f'Best fitness after time limit per tool')
        ax.set_ylabel("Fitness", fontsize=12)
    ax.set_xlabel('Tools', fontsize=12)

    ax.set_ylim(ymin=0)
    plt.savefig(f"plots/{example}_{col_name}_{mode}.pdf")
    plt.close()


if __name__ == '__main__':
    
    examples = sys.argv[1:]

    # Obtain the generation files to make the plots
    ponyge_gens = helper.import_data(examples, 'results/ponyge/', 'generations', ',')
    gengy_gens = helper.import_data(examples, 'results/gengine/', 'generations', ',')

    # Obtain the timer files to make the plots
    ponyge_timer = helper.import_data(examples, 'results/ponyge/', 'timer', ',')
    gengy_timer = helper.import_data(examples, 'results/gengine/', 'timer', ',')
    helper.create_folder("plots/")


    # #########################################################################
    # Generate the gens plot files
    for example in examples:
    
        if not example in ponyge_gens or example in gengy_gens:
            pass
        
        ponyge_df = ponyge_gens[example]
        gengine_df = gengy_gens[example]

        cols = ['processing_time', 'evolution_time']

        # Convert from ns to s
        for df, column in itertools.product([ponyge_df, gengine_df], cols):
            df[column] = df[column].apply(lambda x: x * pow(10, -9))
        
        ponyge_df['total'] = ponyge_df['processing_time'] + ponyge_df['evolution_time']
        gengine_df['total'] = gengine_df['processing_time'] + gengine_df['evolution_time']

        plot_df(ponyge_df, gengine_df, example, 'processing_time', 'generations')
        plot_df(ponyge_df, gengine_df, example, 'evolution_time', 'generations')
        plot_df(ponyge_df, gengine_df, example, 'total', 'generations')

    # #########################################################################
    # Generate the timer plot files
    for example in examples:

        if not example in ponyge_timer or example in gengy_timer:
            pass
        
        ponyge_df = ponyge_timer[example]
        gengine_df = gengy_timer[example]

        cols = ['best_fitness']

        # Convert from ns to s
        for df, column in itertools.product([ponyge_df, gengine_df], cols):
            df[column] = df[column].apply(lambda x: x * pow(10, -9))
        
        plot_df(ponyge_df, gengine_df, example, 'best_fitness', 'timer')
        plot_df(ponyge_df, gengine_df, example, 'best_fitness', 'timer')
        