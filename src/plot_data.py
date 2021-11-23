import sys
import src.evaluation.helper as helper

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def boxplot_df(ponyge_df, gengine_df, example, description):
    ponyge_vals = ponyge_df[description].values
    gengine_vals = gengine_df[description].values

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.violinplot([np.log10(ponyge_vals), np.log10(gengine_vals)])
    tix = ['PonyGE', 'GeneticEngine']
    plt.xticks([1,2], tix, rotation=0, fontsize=12)
    plt.title(f"{description.capitalize()} time per Tool")
    ax.set_ylabel("Time log(ns)", fontsize=12)
    ax.set_xlabel('Tools', fontsize=12)

    plt.savefig(f"plots/{example}_{description}.pdf")
    plt.close()


if __name__ == '__main__':
    
    examples = sys.argv[1:]

    ponyge_times = helper.import_data(examples, 'results/ponyge/', ',')
    gengine_times = helper.import_data(examples, 'results/gengine/', ',')
    
    helper.create_folder("plots/")

    for example in examples:
    
        if not example in ponyge_times or example in gengine_times:
            pass
        
        ponyge_df = ponyge_times[example]
        gengine_df = gengine_times[example]

        ponyge_df['total'] = ponyge_df['processing_time'] + ponyge_df['evolution_time']
        gengine_df['total'] = gengine_df['processing_time'] + gengine_df['evolution_time']

        boxplot_df(ponyge_df, gengine_df, example, 'processing_time')
        boxplot_df(ponyge_df, gengine_df, example, 'evolution_time')
        boxplot_df(ponyge_df, gengine_df, example, 'total')