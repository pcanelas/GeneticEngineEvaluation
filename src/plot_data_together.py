import sys
import src.ponyge_comparison.helper as helper

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_df(merged_dataframe, plot_info):
    
    ax = sns.boxplot(data=merged_dataframe)
    
    tix = ['classification', 'game_of_life', 'median', 'number_io', 'regression', 'smallest', 'string_match', 'sum_of_squares', 'vectorial']
    #tix = "abcdefghi"
    plt.xticks([0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5], tix, rotation=45, fontsize=8)
    plt.title("Titulo temporario")
    
    ax.set_ylabel("Relative performance", fontsize=12)
    #ax.set_xlabel('Tools', fontsize=12)

    ax.set_ylim(ymin=0)
    
    plt.axvline(1.5, ls="--")
    plt.tight_layout()
    plt.savefig(f"merged_plots.pdf")
    plt.close()





if __name__ == '__main__':
    sns.set_theme(style="whitegrid")

    examples = sys.argv[1:]

    # Obtain the generation files to make the plots
    ponyge_gens = helper.import_data(examples, 'results/ponyge_comparison/ponyge/', 'generations', ',')
    gengy_gens = helper.import_data(examples, 'results/ponyge_comparison/gengine/', 'generations', ',')

    # Obtain the timer files to make the plots
    ponyge_timer = helper.import_data(examples, 'results/ponyge_comparison/ponyge/', 'timer', ',')
    gengy_timer = helper.import_data(examples, 'results/ponyge_comparison/gengine/', 'timer', ',')
    helper.create_folder("plots/")

    plot_info = {'title': '',
        'mode': '',
        'column': '',
        'example': '',
    }

    # #########################################################################
    # Create the total performance column
    for example in examples:
        if not example in ponyge_gens or not example in gengy_gens:
            continue
        
        ponyge_df = ponyge_gens[example]
        gengine_df = gengy_gens[example]

        cols = ['processing_time', 'evolution_time']

        # Convert from ns to s
        for df, column in itertools.product([ponyge_df, gengine_df], cols):
            df[column] = df[column].apply(lambda x: x * pow(10, -9))
        
        ponyge_df['total'] = ponyge_df['processing_time'] + ponyge_df['evolution_time']
        gengine_df['total'] = gengine_df['processing_time'] + gengine_df['evolution_time']
    
    
    # #########################################################################
    # Create the Merged Plot of time
    cols = ['Tool', 'Benchmark', 'Time']
    rows = []

    for column, example in enumerate(examples):
        if not example in ponyge_gens or not example in gengy_gens:
            continue
        
        ponyge_df = ponyge_gens[example]
        gengine_df = gengy_gens[example]

        ponyge_rows = list(ponyge_df['total'].values)
        gengine_rows = list(gengine_df['total'].values) 
        
        for val in ponyge_rows:
            rows.append(['PonyGE2', example, val])
        
        for val in gengine_rows:
            rows.append(['GEngine', example, val])
        
    merged_dataframe =  pd.DataFrame(data=rows, columns=cols)
    
    # Calculate the average
    print(merged_dataframe)

    merged_dataframe['Relative Time'] = merged_dataframe.apply(lambda x: x['Time'] / merged_dataframe[merged_dataframe['Tool'].str.contains('PonyGE2') & merged_dataframe['Benchmark'].str.contains(x['Benchmark'])].mean(), axis=1)

    axis = sns.barplot(data=merged_dataframe, x='Benchmark', y='Relative Time', hue='Tool')

    for item in axis.get_xticklabels():
        item.set_rotation(25)

    plt.title("Relative Time of PonyGE2 and GeneticEngine")
    plt.tight_layout()
    plt.savefig(f"merged_plots_time.pdf")
    plt.close()


    # #########################################################################
    # Create the Merged Plot of Fitness

    cols = ['Tool', 'Benchmark', 'Fitness']
    rows = []

    for column, example in enumerate(examples):
        if not example in ponyge_gens or not example in gengy_gens:
            continue
        
        ponyge_df = ponyge_timer[example]
        gengine_df = gengy_timer[example]

        ponyge_rows = list(ponyge_df['best_fitness'].values)
        gengine_rows = list(gengine_df['best_fitness'].values) 
        
        for val in ponyge_rows:
            rows.append(['PonyGE2', example, val])
        
        for val in gengine_rows:
            rows.append(['GEngine', example, val])
        
    merged_dataframe =  pd.DataFrame(data=rows, columns=cols)
    
    # Calculate the average
    print(merged_dataframe)

    merged_dataframe['Relative Fitness'] = merged_dataframe.apply(lambda x: x['Fitness'] / merged_dataframe[merged_dataframe['Tool'].str.contains('PonyGE2') & merged_dataframe['Benchmark'].str.contains(x['Benchmark'])].mean(), axis=1)

    axis = sns.barplot(data=merged_dataframe, x='Benchmark', y='Relative Fitness', hue='Tool')

    for item in axis.get_xticklabels():
        item.set_rotation(25)

    plt.title("Relative Fitness of PonyGE2 and GeneticEngine")
    plt.tight_layout()
    plt.savefig(f"merged_plots_fitness.pdf")
    plt.close()