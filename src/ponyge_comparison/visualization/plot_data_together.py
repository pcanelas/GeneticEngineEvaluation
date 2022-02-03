import sys
import src.helper as helper

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
import seaborn as sns

# def plot_df(merged_dataframe, plot_info):
    
#     ax = sns.boxplot(data=merged_dataframe)
    
#     tix = ['classification', 'game_of_life', 'median', 'number_io', 'regression', 'smallest', 'string_match', 'sum_of_squares', 'vectorial']
#     #tix = "abcdefghi"
#     plt.xticks([0.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5], tix, rotation=45, fontsize=8)
#     plt.title("Titulo temporario")
    
#     ax.set_ylabel("Relative performance", fontsize=12)
#     #ax.set_xlabel('Tools', fontsize=12)

#     ax.set_ylim(ymin=0)
    
#     plt.axvline(1.5, ls="--")
#     plt.tight_layout()
#     plt.savefig(f"plots/merged_plots.pdf")
#     plt.close()


def draw_barplot(df: pd.DataFrame, outbasename: str, what_to_plot: str = "Fitness"):
    """
    Draws a barplot that compares the two tools 
    relatively to some metric passed in the 'what_to_plot' 
    argument, for all the existing examples.
    """
    
    df['Relative {}'.format(what_to_plot)] = df.apply(lambda x: x[what_to_plot] / 
                                                      df[df.Tool.str.contains('PonyGE2') & df.Benchmark.str.contains(x.Benchmark)].mean(), axis=1)

    axis = sns.barplot(data=df, 
                       x='Benchmark', 
                       y='Relative {}'.format(what_to_plot), 
                       hue='Tool')

    for item in axis.get_xticklabels():
        item.set_rotation(25)

    #plt.title("Relative Fitness of PonyGE2 and GeneticEngine")
    plt.tight_layout()
    plt.savefig("plots/{}.pdf".format(outbasename))
    plt.close()
    
def draw_violin_with_facets(df:pd.DataFrame, outbasename: str, what_to_plot: str = "Fitness"):
    """
    Draws violin plots for all examples.
    
    Each facet represents an example, which
    allows for the scale of the 'what_to_plot' to reflect
    absolute values, rather than relative.
    """
    melt_data = data.melt(id_vars=['max_depth', 'tool'], var_name='Benchmark', value_name='Fitness')

    to_replace = {'classification': 'classification (higher_is_better)',
                'game_of_life': 'game_of_life (higher_is_better)',
                'regression': 'regression (lower_is_better)',
                'string_match': 'string_match (lower_is_better)',
                'vectorialgp': 'vectorialgp (lower_is_better)'}

    melt_data = melt_data.replace(to_replace)

    palette ={"PonyGE2": "steelblue", "GeneticEngine": "pink"}
    fig = plt.figure(figsize=(8,6))
    g = sns.catplot(x='max_depth', y='Fitness', hue='tool',
                    sharey=False,
                    sharex=False,
                    palette=palette,
                    height=3, 
                    aspect=1,
                    kind='violin',
                    col='Benchmark',
                    col_wrap=3,
                    data=melt_data)

    (g.set_axis_labels("Max tree depth", "Fitness")
    .set_titles("{col_name}")
    .despine(left=True))  

    g.savefig('test.pdf')



if __name__ == '__main__':
    sns.set_theme(style="whitegrid")

    examples = sys.argv[1:]

    # Obtain the generation files to make the plots
    ponyge_gens = helper.import_data(examples, 'results/ponyge/', 'generations', ',')
    gengy_gens = helper.import_data(examples, 'results/gengine/', 'generations', ',')

    # Obtain the timer files to make the plots
    ponyge_timer = helper.import_data(examples, 'results/ponyge/', 'timer', ',')
    gengy_timer = helper.import_data(examples, 'results/gengine/', 'timer', ',')
    helper.create_folder("plots/")

    plot_info = {'title': '',
        'mode': '',
        'column': '',
        'example': '',
    }


    # #########################################################################
    # Create the total performance column
    if len(ponyge_gens) == len(gengy_gens) != 0:
        print("Running time per generation plot")
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
        # Create the Merged Plot of time taken to do the evolution
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
        draw_barplot(merged_dataframe, outbasename='merged_plots_time', what_to_plot='Time')
       

    # #########################################################################
    # Create the Merged Plot of Fitness in timer mode
    if len(ponyge_timer) == len(gengy_timer) != 0:
        print("Running fitness within time limit plot")

        cols = ['Tool', 'Benchmark', 'Fitness']
        rows = []

        for column, example in enumerate(examples):
            if not example in ponyge_timer or not example in gengy_timer:
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
        
        draw_barplot(merged_dataframe, outbasename='merged_plots_fitness', what_to_plot='Fitness')

       
        plot
