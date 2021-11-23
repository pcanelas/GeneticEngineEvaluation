import sys
import src.evaluation.helper as helper

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    examples = sys.argv[1:]

    ponyge_times = helper.import_data(examples, 'results/ponyge/', ',')
    gengine_times = helper.import_data(examples, 'results/gengine/', ',')
    print(examples)
    for example in examples:
        print(example)
        if not example in ponyge_times or example in gengine_times:
            pass
        
        ponyge_df = ponyge_times[example]
        gengine_df = gengine_times[example]

        tp1 = ponyge_df['processing_time'].values
        tp2 = gengine_df['processing_time'].values

        et1 = ponyge_df['evolution_time'].values
        et2 = gengine_df['evolution_time'].values

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.boxplot([tp1, tp2])
        tix = ['PonyGE', 'GeneticEngine']
        plt.xticks([1,2], tix, rotation=0, fontsize=12)
        plt.title("Processing time per Tool")
        ax.set_ylabel("Time (ns)", fontsize=12)
        ax.set_xlabel('Tools', fontsize=12)

        plt.savefig(f"{example}_processing.pdf")
        plt.close()


        fig2 = plt.figure()
        ax = fig2.add_subplot(1, 1, 1)
        ax.boxplot([et1, et2])
        tix = ['PonyGE', 'GeneticEngine']
        plt.xticks([1,2], tix, rotation=0, fontsize=12)
        plt.title("Evolution time per Tool")
        ax.set_ylabel("Time (ns)", fontsize=12)
        ax.set_xlabel('Tools', fontsize=12)

        plt.savefig(f"{example}_evolution.pdf")